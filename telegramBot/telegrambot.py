import requests
import json
import os
token = dict(os.environ)
token = token['TOKEN']
url = f'https://api.telegram.org/bot{token}/'

def getLastMessage():
    r = requests.get(url+'getUpdates')
    data = r.json()
    data = data['result']
    if len(data):
        data = data[len(data)-1]
        return data
    else:
        return 0

def bot(methods, data = {}):
    r = requests.post(url + methods, data=data)
    data = r.json()
    # print(data)

def button(data = {}):
    r = requests.post(url + 'sendMessage', json=data)
    data = r.json()