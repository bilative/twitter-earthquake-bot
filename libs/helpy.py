import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
import urllib.request
import time
import tweepy
import datetime


# init date
URL = 'http://www.koeri.boun.edu.tr/scripts/lst9.asp'

auth = tweepy.OAuthHandler(my_CONSUMER_KEY, my_CONSUMER_SECRET)
auth.set_access_token(my_ACCESS_TOKEN, my_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Autontatication Error!!!")


api = tweepy.API(auth, wait_on_rate_limit=True,
                wait_on_rate_limit_notify=True)


# I wrote this to handle <pre> form table
def splitIt(row):
    while True:
        row2 = row.replace('   ', '  ')
        if (row == row2):
            break
        else:
            row = row2
    return row

def checkWebsite(last):
    response = urllib.request.urlopen(URL)
    html = response.read()

    soup = BeautifulSoup(html,"lxml")
    data = soup.find("pre").contents[0]

    data = soup.find("pre").find(text=True)

    eachRows = []
    for i in range(5):
        eachRows.append(splitIt(data.split('\n')[7+i]).split('  '))

    df = pd.DataFrame(eachRows)
    df.columns = splitIt(data.split('\n')[5]).split('  ')
    df['Tarih'] = pd.to_datetime(df['Tarih'])

    df = df[ df['Tarih'] > last]

    return df
