import tweepy
import time

consumer_key = 'fHMwl5izOPQ6T57bvC3gJTfVy'
consumer_secret = 'RCcHkdBz6PrJQK03UosfefhVLi5z7PyRqaisoHp9movHQY4Kcz'
access_token = '1230189679636615170-05B5krNtGB58R6cFXyXAFy8pmimP2y'
access_token_secret = 'ABlrkKlXH1xBgRQTQadV8pYjvjrHrxj38H3Lz34YFoQCH'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# api.update_status("this is a tweet from python.")

print("working...")

since_id = 1230251765490233344

while True:

    for tweet in api.home_timeline(since_id):
        api.retweet(tweet.id)
        since_id = tweet.id
    
    sleep(60)