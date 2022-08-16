import json


# returns a list with the top 10 most retweeted tweets
# each tweet is a python dict
# dataset_path is the path to the dataset file
def find_most_retweeted_tweets(dataset_path):
    file = open(dataset_path)
    tweets = json.load(file)
    most_retweeted_tweets = []
    min_retweets = 0
    for tweet in tweets:
        if len(most_retweeted_tweets) < 10:
            most_retweeted_tweets.append(tweet)
        elif len(most_retweeted_tweets) >= 10:
            min_retweets = most_retweeted_tweets[0]["retweetCount"]
            for item in most_retweeted_tweets:
                if min_retweets > item["retweetCount"]:
                    min_retweets = item["retweetCount"]
            if min_retweets < tweet["retweetCount"]:
                most_retweeted_tweets.append(tweet)
                least_retweeted = most_retweeted_tweets[0]
                for item in most_retweeted_tweets:
                    if least_retweeted["retweetCount"] > item["retweetCount"]:
                        least_retweeted = item
                most_retweeted_tweets.remove(least_retweeted)
                min_retweets = most_retweeted_tweets[0]["retweetCount"]
                for item in most_retweeted_tweets:
                    if item["retweetCount"] < min_retweets:
                        min_retweets = item["retweetCount"]
    return most_retweeted_tweets

