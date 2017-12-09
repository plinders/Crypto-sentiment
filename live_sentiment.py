from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import csv
from datetime import datetime
from credentials import *
from textblob_analysis import *

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        try:
            tweet = all_data["text"]


            user = all_data["user"]["id_str"]
            followers = all_data["user"]["followers_count"]
            (sentiment, subjectivity) = get_tweet_sentiment(tweet)
            #score = 0
            weighted = sentiment * (followers / 10000)
            ts = datetime.strptime(all_data["created_at"], '%a %b %d %H:%M:%S %z %Y')

            print(tweet, sentiment, followers, weighted)
            #print("Tweet sentiment = {}, tweet subjectivity = {}".format(sentiment, subjectivity))

            with open("twitter-out.txt", "a") as f:
                #f.write('Time,Text,Followers,Score,Weighted_score')
                writer = csv.writer(f)
                writer.writerow([ts, tweet, user, followers, sentiment, weighted])

        except KeyError:
            pass


        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["$btc", "$BTC", "#bitcoin", "#Bitcoin"], languages=["en"], async=True)
