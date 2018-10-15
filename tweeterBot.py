from generateMarkovText import make_poem
import tweepy
import pickle
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
chain = pickle.load(open("chain.pkl", "rb"))

while True:
    tweet = generateMarkovText()
    api.update_status(tweet)
    time.sleep(21600)



poem = make_poem(chain)
print(poem)
