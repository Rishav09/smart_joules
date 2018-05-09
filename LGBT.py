from textblob import TextBlob
import tweepy,sys
import csv
import pandas as pd
import matplotlib.pyplot as plt

consumer_key = 'GdK7gzRCu28DqB2D0flGubF00'
consumer_secret = 'JWpOhvEFE4RX1DyJoB3cZMnxlweWaxMhyqVqeivF3LK9x7H0wb'
access_token = '928950395854114818-26BORYbxdcULEXUxhlOkQ87NwusfPCx'
access_token_secret = '7F5AIeAUtdcUlyoMstaSsNdOJb8wNCuHmWNhYNQTffy5A'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('lgbt.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

tweets= tweepy.Cursor(api.search,q="#LGBT",count=100,
                           lang="en").items(100)


def percentage(part,whole):
	return 100*float(part)/float(whole)

positive=0
negative=0
neutral=0
polarity=0

for tweet in tweets:
	analysis=TextBlob(tweet.text)
	polarity+=analysis.sentiment.polarity

	if(analysis.sentiment.polarity==0.00):
		neutral+=1
	elif(analysis.sentiment.polarity<0.00):
		negative+=1
	else:
		positive+=1

positive=percentage(positive,100)
negative=percentage(negative,100)
neutral=percentage(neutral,100)
polarity=percentage(polarity,100)

if(polarity==0):
	print("Neutral")
elif(polarity<0):
	print("Negative")
else:
	print("positive")

labels=['Positive['+str(positive)+'%]','Neutral['+str(neutral)+ '%]','Negative['+str(negative)+'%]']
sizes=[int(positive),int(neutral),int(negative)]
colors=['yellowgreen','gold','red']
patches,texts=plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title("LGBT")
plt.axis('equal')
plt.show()

















