import tweepy
import API_STUFF

BEARER_TOKEN=API_STUFF.BEARER_TOKEN

API_KEY='foo'
API_SECRET = 'baar'
ACCESS_TOKEN = 'faar'
access_tken='boo'

auth = tweepy.OAuth1UserHandler(BEARER_TOKEN)


api=tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)