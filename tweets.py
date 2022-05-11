#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:47:35 2022

@author: lymenbae
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
import csv
import os
import urllib.request
import json
import nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()
from textblob import TextBlob
import tweepy
import yaml
from collections import Counter
from unidecode import unidecode
import torch
import transformers
#%%

#Looking at the twitter analysis
twitter_url='https://twitter.com/home?lang=ru'
#The step above gets the results from the twitter page
query="#Ukraine"
#ANalyzing twitter tweets from March 2nd
twitter=pd.read_csv("UkraineCombinedTweetsDeduped_MAR02.csv")
twitter.head()
#Opening up all of the tweets
twitter.info()
#Sorting in order
twitter.isna().sum().sort_values(ascending=False)
#Looking at the language of the tweets
twitter.language.value_counts()
#english is 274540
#french:22922
#undefined:16228
#%%
#Looks at the most retweeted tweets on March 2nd
tweets = twitter[['username', 'text','retweetcount','tweetid', ]].sort_values(by = 'retweetcount', ascending=False)
most_retweeted=tweets.iloc[-8]
print("\n: The most retweeted text is:",most_retweeted.text)

tweets = twitter[['username', 'text','retweetcount','tweetid', ]].sort_values(by = 'retweetcount', ascending=False)
most_retweeted=tweets.iloc[0]
print("\n: The most retweeted text is:",most_retweeted.text)
#The most retweeted text is: .@ZelenskyyUa's tv address to the Russian (!) people might be the most moving speech that I've ever seen in my entire life. 
#The whole world needs to see, understand and share this crucial Ukrainian message.
#StandWithUkraine #Ukraine #Україна #Russia #Россия https://t.co/WoMOgqXTWX
#The most retweeted text is: @NATO, close the sky over #Ukraine

tweet_en=twitter[twitter.language=='en'].drop('language',axis=1)
tweets=tweet_en[['username', 'text','retweetcount','tweetid', ]].sort_values(by = 'retweetcount', ascending=False)
tweets.head(15)
tweet_en.location.value_counts()[:20].plot.bar().set_title="Most tweets by country"

#Sort by users who tweet in english:
#Creating columns that will show time as a feature:
time_cols = ['extractedts','tweetcreatedts','usercreatedts']
tweet_en[time_cols[2]]=pd.to_datetime(tweet_en[time_cols[2]])
#Sorting by the date of creation in ascending order:
columns=tweet_en.columns.to_list()
users=tweet_en.sort_values(by =  time_cols[2], ascending=True)
users.head(100)

#Looking at  total tweets over March 2nd, April 1st, and April 20th

twitter2 = pd.read_csv("0401_UkraineCombinedTweetsDeduped.csv")
twitter3 = pd.read_csv("0420_UkraineCombinedTweetsDeduped.csv")
total_tweets = pd.concat([twitter, twitter2, twitter3])
#Twitter tweets by language
total_tweets.language.value_counts()
total_tweets_en = total_tweets[total_tweets.language == 'en'].drop('language', axis=1)
#Plotting the total tweets by location over the 3 spots
fig,ax1 = plt.subplots()
total_tweets_en.location.value_counts()[:20].plot(kind='barh',figsize=(7, 6))
plt.xlabel("Tweets")
plt.ylabel("Country")
plt.title("Most Tweets by Country")
fig.savefig("Total tweets by the country over 3 days.png")

#Analyzing the hashtags
num_chars = total_tweets_en.text.apply(len) #looking at the length of teh characters
#apply() function calls the lambda function and applies it to every row or column of the dataframe and returns a modified copy of the dataframe:
num_words = total_tweets_en.text.apply(lambda x: len(x.split()))
total_tweets_en['num_chars'] = num_chars
total_tweets_en['num_words'] = num_words

total_tweets_en.groupby('num_chars')['retweetcount','favorite_count'].describe()
#Looking at what are the most popular hashtags that were used over those 3 days
def evaluate_hashtags(x):
    hashtags = []
    
    a = eval(str(x))
    
    for item in a:
        hashtags.append((str(unidecode(item["text"])).lower()))
        hashtags = list(set(hashtags))
#The step above is evaluating whether the hashtag is actually a text message, instead of the number    
    return hashtags
#Creating an empty list to combine the hashtags with text into one format
masterlist = []
hashtagsListCollection = total_tweets["hashtags"].apply(evaluate_hashtags)

for hashtagsList in hashtagsListCollection:
    for hashtag in hashtagsList:
        masterlist.append(hashtag)
#Looking at the 25 most retweeted ones
topXItem = 25 
x = Counter(masterlist)
topXItemList = x.most_common(topXItem)
#Making it into the pandas dataframe, so that it would be easier to look at
hash = pd.DataFrame(topXItemList)
hash.columns =['Hashtag','Tweets']
hash
#Plotting the results:
fig,ax1=plt.subplots()
plt.rcParams["figure.figsize"] = [20, 6]
hash.plot.bar(x='Hashtag', y='Tweets', rot=90,color='green')
plt.xlabel("Hashtags")
plt.ylabel("Count")
plt.title("Most Popular Hashtags")
fig.savefig("Hashtags  over 3 days.png")

doc='twitter_config.yaml'
with open(doc) as f:
    config = yaml.safe_load(f)
    
#Setting up Twitter API
auth = tweepy.OAuthHandler(config['CONSUMER_KEY'],config['CONSUMER_SECRET'])
auth.set_access_token(config['OAUTH_TOKEN'],config['OAUTH_SECRET'])
api = tweepy.API(auth)

#Going to work with BBC News
# Employee Class
def method(self, 'BBCWorld')
BBC_timeline = api.user_timeline('BBCWorld'=='BBCWorld')
type(BBC_timeline)

#Converting it into json
BBCWorld_list=list(BBC_timeline)
BBC_json=[tweet._json for tweet in BBC_timeline]
BBC_json

#Creating a dataframe, which would also make it easier to work with
BBC_df = pd.DataFrame(BBC_json)
BBC_df.head()

#Looking at what are the most popular words used in BBC World News and what is its frequency
import nltk
nltk.download('punkt')
BBC_l = [doc['text'] for doc in BBC_json if 'text' in doc.keys()]
BBC_tokens = [tok for tweet in BBC_l for tok in nltk.word_tokenize(tweet)]
BBC_tokens

#Removing the punctuation
#This allows to take in a word, and return True only if it has no letters in it
import re
def alpha_filter(w):
    pattern = re.compile('^[^a-z]+$')
    if (pattern.match(w)):
        return True
    else:
        return False
#Removes the punctuation as the most popular word from out list

  
    