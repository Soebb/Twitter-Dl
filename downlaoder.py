from tweepy import OAuthHandler, API
from decouple import config


auth = OAuthHandler(
    config('CONSUMER_KEY'),
    config('CONSUMER_SECRET_KEY')
)
auth.set_access_token(
    config('TWITTER_ACCESS_TOKEN'),
    config('TWITTER_ACCESS_TOKEN_SECRET')
)

api = API(auth)


def download_tweet(tweet_url):
    try:
        tweet_id = tweet_url.split('status/')[-1].split('?')[0]
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


print(download_tweet('https://twitter.com/michaelkutsche/status/1446270542005243920'))