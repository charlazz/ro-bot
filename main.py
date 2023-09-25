from api_keys import *
import tweepy 



# Identifiants de l'apllication 
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message,image_path)

    else: 
        api.update_status(message)

        print('Tweeted successfully')


if __name__ == '__main__':
   
    tweet(twitter_api, '25231.png')
            


     








#class MyStreamListener(tweepy.StreamListener):
    #def __init__(self,api):
     #   self.api = api
      #  self.me = api.me()

    #def on_status(self,tweet):
     #   while(1):
      #      try: 
       #         print(tweet.user.name) # affiche le nom du user
        #        print(tweet.text) # affiche let texte du tweet
         #       self.api.create_favorite(tweet.id) # creation du fav
          #  except (tweepy.TweepError):
           #     return True # gestion de l'exception 
            
    #def on_error(self,status):
     #   print ("Error detected")

      #  tweets_listener = MyStreamListener(api)
       # stream = tweepy.Stream(api.auth, tweets_listener)
        #stream.filter(track=["programmation", ""])
