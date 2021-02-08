import requests
import json
import os
apiKey = dict(os.environ)
apiKey = apiKey['APIKEY']
def getCorrencies():
    url = f'https://free.currconv.com/api/v7/currencies?apiKey={apiKey}'
    r = requests.get(url)
    data = r.json()
    return data['results']

def correnyConvert(amount, fromCurrency, toCurrency):
    url = 'https://free.currconv.com/api/v7/convert'
    tmp = fromCurrency + '_' + toCurrency
    params = {
        'apiKey' : apiKey,
        'q' : tmp,
        'compact' : 'ultra'
    }
    r = requests.get(url,params=params)
    data = r.json()
    return data[tmp]*amount