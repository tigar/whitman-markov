from generateMarkovText import make_poem
import tweepy
import time
import pickle
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

print(CONSUMER_KEY, CONSUMER_SECRET)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
chain = pickle.load(open("emerson_whitman.pkl", "rb"))

while True:
    tweet = make_poem(chain)
    print(tweet)
    api.update_status(tweet)
    time.sleep(21600)
