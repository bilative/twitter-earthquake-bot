import time
import tweepy
import datetime

auth = tweepy.OAuthHandler(my_CONSUMER_KEY, my_CONSUMER_SECRET)
auth.set_access_token(my_ACCESS_TOKEN, my_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Autontatication Error!!!")


api = tweepy.API(auth, wait_on_rate_limit=True,
                wait_on_rate_limit_notify=True)