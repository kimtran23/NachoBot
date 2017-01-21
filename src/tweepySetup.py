import tweepy

auth = tweepy.OAuthHandler("P59fg00MtbVNnd0YR9Zq1TZJv",
                           "mJxrGLjiqcDREuI5ow3iBNuEyUjDQNsQgqm6jXJKL2BibuBXtD")
auth.set_access_token("63926897-UyXhEiGXD3mhnRbUvaeEOsayiYTykCEWACyYBrFoe",
                      "cV1tEVIXwUF9kdUfipekTTqYIWDSMjY3UFzxpxa8k7MSq")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
