import tweepy
from textblob import TextBlob
import csv
import json
import credentials.twitter as creds

oscar_noms = [
    'Parasite'
    '1917',
    'Ford v Ferrari',
    'Joker',
    'Once Upon a Time in Hollywood',
    'Parasite',
    'The Irishman',
    'Little Women',
    'Jojo Rabbit',
    'Marriage Story'
]
context = ['film', 'movie', 'oscar', 'cinema']

print(oscar_noms)
print(context)

consumer_key = creds.API_KEY
consumer_secret = creds.API_SECRET_KEY
access_token = creds.API_ACCESS_TOKEN
access_token_secret = creds.API_ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

parasite_tweets = api.search('parasite film', count=10)

print(type(parasite_tweets))
# print('***********')
# print(parasite_tweets)
