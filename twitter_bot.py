import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


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

    print("updated")
    
    time.sleep(60)