import sys

from decouple import config
from tweepy import API, OAuthHandler


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


api.update_status(
    status='Hello World @Hemmatkia',
    in_reply_to_status_id=1446883272819150854
)

api.update_status