# NOTE: follow this twitter bot @2021Gators on Twitter

import tweepy
import time
import datetime

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# api.update_status("this is a tweet from python.")

print("working...")

# print(api.home_timeline()[0].user.screen_name)

# find the most recent id from tweets on the timeline
since_id = api.home_timeline()[0].id

# api.hometimeline() returns a list of status objects
# to get the most recent one, access the first element in the list

while True:

    # initialize count to zero
    count = 0

    print("There is/are " + str(len(api.home_timeline(since_id))) +
          " tweet(s) being processed")

    # loop through all tweets since the last "since_id"
    for tweet in api.home_timeline(since_id):

        count = count + 1

        # Retweet original tweets that have gained at least 8 favorites in the tweet's first 3 minutes

        # create a condition here where the tweet must be over 10 minutes old
        if datetime.datetime.utcnow() - tweet.created_at >= datetime.timedelta(0, 3*60):

            lowerTweet = str.lower(tweet.text)
            lowerTweetList = lowerTweet.split(" ")

            specialWordsExact = ["uf"]
            specialWordsInexact = ["gainesville", "university of florida", "gator", "swamp", "🐊", "commit","chomp","mullen"]

            containsSpecialWord = False

            for word in specialWordsInexact:
                if word in lowerTweet:
                    containsSpecialWord = True
                    specialWord = word
                    break
            
            if containsSpecialWord == False:
                for tweetWord in lowerTweetList:
                    for specialWordExact in specialWordsExact:
                        if tweetWord == specialWordExact:
                            containsSpecialWord = True
                            specialWord = tweetWord
                            break
                    if containsSpecialWord:
                        break

            try:
                # do not retweet retweets
                # every retweet starts with "RT @"
                if "RT @" not in tweet.text:
                    # retweet it tweet has over 19 likes
                    if tweet.favorite_count >= 8:
                        api.retweet(tweet.id)
                        print("Tweet " + str(count) + ": " + "\"" + tweet.text + "\"" + " from @" +
                              tweet.user.screen_name + " was retweeted. Had " + str(tweet.favorite_count) + " favorite(s).")
                    # retweet if tweet contains certain key words
                    elif containsSpecialWord == True:
                        api.retweet(tweet.id)
                        print("Tweet " + str(count) + ": " + "\"" + tweet.text + "\"" + " from @" +
                              tweet.user.screen_name + " was retweeted. Contained the special word " + specialWord + " but only had " + str(tweet.favorite_count) + " favorite(s).")
                    else:
                        print("Tweet " + str(count) + ": " + "\"" + tweet.text + "\"" + " from @" +
                              tweet.user.screen_name + " was not retweeted. Had " + str(tweet.favorite_count) + " favorite(s) and did not contain a special word.")
                else:
                    print("Tweet " + str(count) + ": " + "\"" + tweet.text + "\"" + " from @" +
                          tweet.user.screen_name + " is a retweet, so it will be ignored.")
            # if the tweet has already been retweeted, and error will be thrown
            except:
                print(
                    "Error was thrown because the tweet being retweeted has already been retweeted")
                since_id = tweet.id
                continue

            since_id = tweet.id
        else:
            print("Tweet " + str(count) + ": " + "\"" + tweet.text + "\"" +
                  " from @" + tweet.user.screen_name + " is less than 3 minutes old.")

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    print("updated at " + current_time)
    print("____________________________________________________________________")

    time.sleep(60*2)
