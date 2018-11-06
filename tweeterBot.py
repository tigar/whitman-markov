from generateMarkovText import make_bigram_poem
import tweepy
import time
import pickle
import random
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

print(CONSUMER_KEY, CONSUMER_SECRET)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
chain = pickle.load(open("pickles/bigramEmersonWhitman.pkl", "rb"))

while True:
    tweet = ""
    for i in range(random.randint(3, 7)):
        new_sentence = make_bigram_poem(chain)
        if i == 0:
            new_tweet = new_sentence
        else:
            new_tweet = tweet + " " + new_sentence
        if len(new_tweet) > 280:
            break
        tweet = new_tweet
    print(tweet)
    api.update_status(tweet)
    time.sleep(21600)