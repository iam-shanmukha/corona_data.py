from covid import Covid
import time
import tweepy

covid = Covid()
India_cases = covid.get_status_by_country_id(27)

############################Twitter########################
consumer_key =environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token =environ['access_token']
access_token_secret =environ['access_token_secret']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for param,val in India_cases.items():
	#print("{} : {}".format(param,val))
	#print(val)
	val = str(val)
	
t=time.ctime(int(val[:10]))

print(f"Last Update : {t}" + "\n".join("{} : \t{}".format(k, v) for k, v in India_cases.items()))
print(t)
api.update_status(status=f"Last Update : {t}" + "\n"+ "\n".join("{} : \t{}".format(k, v) for k, v in India_cases.items()))