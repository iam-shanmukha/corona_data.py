from covid import Covid
import tweepy
from os import *


############################Twitter########################
consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while(1):
	try:
		covid = Covid(source="worldometers")
		India_cases = covid.get_status_by_country_name("india")
		print("\n"+ "\n".join("{} : \t{}".format(k, v) for k, v in India_cases.items() if not k.startswith(('population','total')))+"\n#IndiaFightsCorona")
		api.update_status(status="\n".join("{} : \t{}".format(k, v) for k, v in India_cases.items() if not k.startswith(('population','total')))+"\n#IndiaFightsCorona"))
		print("Tweeted")
	except tweepy.TweepError as e:
		print("Duplicate")