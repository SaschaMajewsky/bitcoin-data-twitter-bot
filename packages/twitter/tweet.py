import tweepy
from packages.fileIO.twitter_api import get_consumer_key, get_consumer_secret, get_access_key, get_access_secret

CONSUMER_KEY = get_consumer_key()
CONSUMER_SECRET = get_consumer_secret()
ACCESS_KEY = get_access_key()
ACCESS_SECRET = get_access_secret()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def send_tweet(content):
    api.update_status(content)
