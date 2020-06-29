from covid import Covid
import time
import tweepy
from os import *

covid = Covid(source="worldometers")
India_cases = covid.get_status_by_country_name("india")
delta_hour = 0
count = 0
############################Twitter########################
consumer_key =environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token =environ['access_token']
access_token_secret =environ['access_token_secret']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while(1):
	try:
			for param,val in India_cases.items():
				val = str(val)
			t=time.ctime(int(val[:10]))
			print(f"{count+1}=>Last Updated : {t}" + "\n"+ "\n".join("{} : \t{}".format(k, v) for k, v in India_cases.items()))
			api.update_status(status=f"{count+1}=>Last Updated : {t}" + "\n"+ "\n".join("{} : \t{}".format(k, v) for k, v in India_cases.items()))
			print("Tweeted")
	except tweepy.TweepError as e:
		print("Duplicate")
