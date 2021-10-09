from tweepy import Stream
from tweepy import OAuthHandler
import tweepy
from tweepy.streaming import Stream as StreamListener
from decouple import config
import json


ckey="EeQuT3VuMHYQ5GJYolkYM7hwS"
csecret="o3f0Mn7oVmBtcz5tHVNzs0tpgzrh6bx2m2tMOGV28q0bSvPzaB"
atoken="1059838453343490048-UmJf2dgEi8Kvdk4IWQ4UQdwXtwDkkh"
asecret="PmxPCUWZz7fwqyPgqNfubJR6suxfvLRC5Vqisi8JN2ygJ"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]

        username = all_data["user"]["screen_name"]

        print((username,tweet))

        return True

    def on_error(self, status):
        print(status)


auth = tweepy.OAuthHandler(
    config('CONSUMER_KEY'),
    config('CONSUMER_SECRET_KEY')
)
auth.set_access_token(
    config('TWITTER_ACCESS_TOKEN'),
    config('TWITTER_ACCESS_TOKEN_SECRET')
)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])