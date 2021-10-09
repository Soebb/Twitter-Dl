from decouple import config
from tweepy import API, OAuthHandler, Stream
from pdb import set_trace

def download_tweet(tweet_id):
    try:
        tweet = api.get_status(tweet_id, tweet_mode="extended")
    except:
        return "Not Found"
    try:
        media = tweet.extended_entities['media']
        urls = []
        for item in media:
            media_type = item['type']
            if media_type == 'photo':
                urls.append(item['media_url_https'])
            elif media_type == 'video':
                video_info = item['video_info']
                media_variants = video_info['variants']
                count = 0
                for item in media_variants:
                    if item['content_type'] == 'application/x-mpegURL':
                        media_variants.pop(count)
                    count += 1
                media_variants.sort(key=lambda x: x['bitrate'], reverse=True)
                urls.append(media_variants[0]['url'])
            elif media_type == 'animated_gif':
                gif_info = item['video_info']
                media_variants = gif_info['variants']
                count = 0
                for item in media_variants:
                    if item['content_type'] == 'application/x-mpegURL':
                        media_variants.pop(count)
                    count += 1
                media_variants.sort(key=lambda x: x['bitrate'], reverse=True)
                urls.append(media_variants[0]['url'])
        return urls
    except AttributeError:
        return "Media Not Found"


class MentionedTweets(Stream):

    def on_status(self, status):
        main_tweet_id = status.in_reply_to_status_id
        user_username = status.user.screen_name
        if main_tweet_id is not None:
            download_data = download_tweet(main_tweet_id)
            if download_data == "Media Not Found":
                api.update_status(
                    status=f"@{user_username} توییت مورد نظر رسانه ای ندارد.",
                    in_reply_to_status_id=status.id,
                )
            else:
                api.update_status(
                    status=f"@{user_username} لینک های دانلود:\n\n" + "\n".join(download_data),
                    in_reply_to_status_id=status.id,
                )


auth = OAuthHandler(
    config('CONSUMER_KEY'),
    config('CONSUMER_SECRET_KEY')
)
auth.set_access_token(
    config('TWITTER_ACCESS_TOKEN'),
    config('TWITTER_ACCESS_TOKEN_SECRET')
)

api = API(
    auth,
    wait_on_rate_limit=True,
)

streamer = MentionedTweets(
    config('CONSUMER_KEY'), config('CONSUMER_SECRET_KEY'),
    config('TWITTER_ACCESS_TOKEN'), config('TWITTER_ACCESS_TOKEN_SECRET')
)

streamer.filter(track=['@matin__b'])
