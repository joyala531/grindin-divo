

import tweepy
from transformers import pipeline

API_KEY = 'DtTT0tJsJoUst6mcJQ3uhqNwL'
API_SECRET = 'KmXW4y3coby3ouiHEtMap1hkp0Dasj5WvZCCFRFqfY4l8bua0o'
ACCESS_TOKEN = '1520275821327310848-1w5RU7PNTNdRQazpj8iXMDwtSHE1lr'
ACCESS_TOKEN_SECRET = 'Mjzg8Hi6uPkaPAPXW7dP74xVpvVszh9rqUXyQHsp0ST0I'

def fetch_tweets(query='stocks', count=10):
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    tweets = api.search_tweets(q=query, lang='en', count=count)
    return [tweet.text for tweet in tweets]

def analyze_sentiment_bert(texts):
    sentiment_model = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')
    results = sentiment_model(texts)
    return results


# Example usage:
def get_tweets_with_sentiment(query='stocks', count=10):
    tweets = fetch_tweets(query, count)
    sentiments = analyze_sentiment_bert(tweets)
    return list(zip(tweets, sentiments))

if __name__ == "__main__":
    results = get_tweets_with_sentiment('stocks', 10)
    for tweet, sentiment in results:
        print(f"Tweet: {tweet}\nSentiment: {sentiment}\n")
