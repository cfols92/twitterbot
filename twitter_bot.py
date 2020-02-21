# NOTE: follow this twitter bot @2021Gators on Twitter

import tweepy
import time
from datetime import datetime

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# api.update_status("this is a tweet from python.")

print("working...")

# print(api.home_timeline()[0].id)

# find the most recent id from tweets on the timeline
since_id = api.home_timeline()[0].id

# api.hometimeline() returns a list of status objects
# to get the most recent one, access the first element in the list

while True:

    # initialize count to zero
    count = 0

    # loop through all tweets since the last "since_id"
    for tweet in api.home_timeline(since_id):
        
        # add condition where the bot retweets only if the tweet is not a retweet

        # try to retweet
        try:
            # do not retweet retweets
            # every retweet starts with "RT"
            if "RT" not in tweet.text:
                api.retweet(tweet.id)
        
        # if the tweet has already been retweeted, and error will be thrown
        except:
            print("Error was thrown because the tweet being retweeted has already been retweeted")
            since_id = tweet.id
            continue
        
        since_id = tweet.id
        count = count + 1

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    print("updated at " + current_time + "\nfound " + str(count) + " new tweets")
    
    time.sleep(60)