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
########################Telegram###########################
import requests
def send_msg(text):
   token = environ['telegram_token']
   chat_id = environ['telegram_chat_id']
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   results = requests.get(url_req)
   print(results.json())
count = 0
while(1):
	try:
		covid = Covid(source="worldometers")
		India_cases = covid.get_status_by_country_name("india")
		#print("\n"+ "\n".join("{} : \t{}".format(k, v) for k, v in India_cases.items() if not k.startswith(('population','total')))+"\n#IndiaFightsCorona")
		stat="\n".join("{} : \t{}".format(k, v) for k, v in India_cases.items() if not k.startswith(('population','total')))+"\n#IndiaFightsCorona"+"\n"+str(count)
		print(stat)
		api.update_status(status=stat) # sending twitter message
		send_msg(stat) ##sending telegram message
		print("Tweeted")
		count = count+1
	except tweepy.TweepError as e:
		print("Duplicate")
