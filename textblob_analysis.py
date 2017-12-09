import re
from textblob import TextBlob

def clean_tweet(tweet):
    '''
    Utility function to clean tweets by removing links, emoticons, special characters
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))

    return(analysis.sentiment.polarity, analysis.sentiment.subjectivity)
