import tweepy
import modules.fileIO.twitter_api

CONSUMER_KEY = modules.fileIO.twitter_api.get_consumer_key()
CONSUMER_SECRET = modules.fileIO.twitter_api.get_consumer_secret()
ACCESS_KEY = modules.fileIO.twitter_api.get_access_key()
ACCESS_SECRET = modules.fileIO.twitter_api.get_access_secret()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def send_tweet(content):
    api.update_status(content)
