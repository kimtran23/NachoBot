import tweepy
import re
auth = tweepy.OAuthHandler("P59fg00MtbVNnd0YR9Zq1TZJv",
                           "mJxrGLjiqcDREuI5ow3iBNuEyUjDQNsQgqm6jXJKL2BibuBXtD")
auth.set_access_token("63926897-UyXhEiGXD3mhnRbUvaeEOsayiYTykCEWACyYBrFoe",
                      "cV1tEVIXwUF9kdUfipekTTqYIWDSMjY3UFzxpxa8k7MSq")

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    try:
        print (tweet.text)
        results=re.sub(r"#\w+","",tweet.text)
        #' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",tweet.text).split())
    except UnicodeEncodeError:
        pass
   
        
            
            
       

    
