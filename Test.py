from core import utils
import pprint
import requests
from decouple import config
import json

NEWS_API_KEY = config('API_KEY')
counry = 'us'

def news():
    latest_news = requests.get(f'https://newsapi.org/v2/top-headlines?country={counry}&apiKey={NEWS_API_KEY}').json()
    
    return latest_news["articles"]

print (news())