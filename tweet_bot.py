from time import sleep

import tweepy
import time
import yweather


def rate_limiter(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1)
    except StopIteration:
        return


def print_trending_in_location(woeid):
    client = yweather.Client()
    # lid = client.fetch_lid()
    # print(f"============ Trending in {lid} ===========")
    trends = api.trends_place(woeid)
    print(trends)


def print_home_timeline():
    print("============Home Timeline==============")
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


def print_follower_names():
    print("============ Followers ===========")
    for follower in rate_limiter(tweepy.Cursor(api.followers).items()):
        print(follower.name)


def follow_back_followers():
    print("============ Following back all the Followers ===========")
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()


def print_folloer_list():
    print("============ Printing follow list ===========")
    for user in rate_limiter(tweepy.Cursor(api.friends).items()):
        print(f"{user.name} | {user.id} | @{user.screen_name}")


def search_tweet(search_string, tweet_count):
    print("============ Search for tweet ===========")
    for tweet in rate_limiter(tweepy.Cursor(api.search, search_string).items(tweet_count)):
        print(tweet.text)


def like_all_from_user(userid):
    print("============ Like all the tweets from a user ===========")
    search_user = userid
    # tweet_count = 10
    user = api.get_user(search_user)
    print(f"Fetching tweets for {search_user}")
    for tweet in rate_limiter(tweepy.Cursor(api.user_timeline, id=search_user).items()):
        # print(tweet._json['favorited'])
        if not tweet._json['favorited']:
            print(f"Bot Liked the tweet ID:{tweet.id}, begins with:{tweet.text[:50]}")
            api.create_favorite(tweet.id)
        else:
            print(f"IGNORE: Bot already Liked the tweet ID:{tweet.id}, begins with:{tweet.text[:50]}")


if __name__ == '__main__':
    auth = tweepy.OAuthHandler('', '')
    auth.set_access_token('',
                          '')
    api = tweepy.API(auth)

    # Print Trending  in India
    client = yweather.Client()
    woeid_India = client.fetch_woeid('India')
    print_trending_in_location(woeid_India)

    # Print Timeline
    print_home_timeline()
