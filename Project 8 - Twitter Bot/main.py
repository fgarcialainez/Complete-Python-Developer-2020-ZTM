"""
This module implements the Twitter bot exercise of the Section 17 of the course.
"""

import time
import tweepy


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)


def twitter_bot():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Print user information
    user = api.me()
    print(user.name)
    print(user.screen_name)
    print(user.followers_count)

    # Be nice to your followers. Follow everyone!
    for follower in limit_handle(tweepy.Cursor(api.followers).items()):
        if follower.name == 'Usernamehere':
            print(follower.name)
            follower.follow()

    # Be a narcisist and love your own tweets. or retweet anything with a keyword!
    number_of_tweets = 2
    search = "zerotomastery"

    for tweet in tweepy.Cursor(api.search, search).items(number_of_tweets):
        try:
            tweet.favorite()
            print('Retweeted the tweet!')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


# Entry point of the script
if __name__ == '__main__':
    # Call the Twitter bot function
    twitter_bot()
