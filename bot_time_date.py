#!sudo pip uninstall twitter -y
#!sudo pip install python-twitter
# read docs: https://python-twitter.readthedocs.io/en/latest/

import json
import os
import requests
import sys
import time
import twitter
from keys import consumer_key, consumer_secret, access_token_key, access_token_secret

api = twitter.Api(consumer_key = consumer_key,
                  consumer_secret = consumer_secret,
                  access_token_key = access_token_key,
                  access_token_secret = access_token_secret)

user = api.VerifyCredentials().AsDict()
print('logged into twitter as "{}" id={}'.format(user['screen_name'], user['id']))

bottweets = "Today is the date: "  + time.strftime("%x") + " and the time is always late: " + time.strftime("%X")
api.PostUpdate(status = bottweets)

print('script finished')
