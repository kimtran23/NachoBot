import tweepy

id = -1
name = ""


def tweetMsg():
    auth = tweepy.OAuthHandler("P59fg00MtbVNnd0YR9Zq1TZJv",
                               "mJxrGLjiqcDREuI5ow3iBNuEyUjDQNsQgqm6jXJKL2BibuBXtD")
    auth.set_access_token("63926897-UyXhEiGXD3mhnRbUvaeEOsayiYTykCEWACyYBrFoe",
                          "cV1tEVIXwUF9kdUfipekTTqYIWDSMjY3UFzxpxa8k7MSq")

    api = tweepy.API(auth)

    tweetlist = list()
    # public_tweets = api.home_timeline()
    public_tweets = api.search(q="%23askYP", count=1)

    for tweet in public_tweets:
        global id
        global name
        id = tweet.id
        name = tweet.user.screen_name

        if tweet.place is not None:
            location = tweet.place.name
        else:
            api.update_status("Hi @{}, we could not locate you. Let us know by #askYP your closest city!".format(
                tweet.user.screen_name), in_reply_to_status_id=tweet.id)
            location = "Montreal"

        print("User: {}, tweet: {}, city: {}".format(
            tweet.user.screen_name, tweet.text, location))

        words = tweet.text.split()
        tweetMsg = ""
        for word in words:
            if ("#" in word or "@" in word or "RT" in word):
                continue
            else:
                tweetMsg += word + " "
        tweetlist.append(tweetMsg)
    return tweetlist


def replyTo(msg):
    auth = tweepy.OAuthHandler("P59fg00MtbVNnd0YR9Zq1TZJv",
                               "mJxrGLjiqcDREuI5ow3iBNuEyUjDQNsQgqm6jXJKL2BibuBXtD")
    auth.set_access_token("63926897-UyXhEiGXD3mhnRbUvaeEOsayiYTykCEWACyYBrFoe",
                          "cV1tEVIXwUF9kdUfipekTTqYIWDSMjY3UFzxpxa8k7MSq")

    api = tweepy.API(auth)
    api.update_status("@{} ".format(name) + msg, in_reply_to_status_id=id)
