import requests
import json
token = ''
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