from typing import Counter
import tweepy
from decouple import config


def download_video(media):
    video_info = media['video_info']
    media_variants = video_info['variants']
    count = 0
    for item in media_variants:
        if item['content_type'] == 'application/x-mpegURL':
            media_variants.pop(count)
        count += 1
    return media_variants
    # media_variants.sort(key=lambda x: x['bitrate'], reverse=True)
    



def downlaod(tweet_id):
    media = api.get_status(tweet_id)
    try:
        media = media.extended_entities['media'][0]
        media_type = media['type']
        if media_type == 'photo':
            return "Its Photo!"
        elif media_type == 'video':
            return download_video(media)
        elif media_type == 'animated_gif':
            return "Its Animated Gif!"
    except AttributeError:
        return "No Media"


auth = tweepy.OAuthHandler(
    config('TWITTER_API_KEY'),
    config('TWITTER_API_SECRET_KEY')
)
auth.set_access_token(
    config('TWITTER_ACCESS_TOKEN'),
    config('TWITTER_ACCESS_TOKEN_SECRET')
)

api = tweepy.API(auth)

print(downlaod("1445802318998298626"))