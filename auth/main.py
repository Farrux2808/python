import requests

headers = {
    'X-API-KEY' : 'bdceb3b6fc0f449f8a950d30e2ad2a09',
}
params = {
   'nameType' : 'fullName',
   'quantity' : 1
}

url = 'https://randommer.io/api/Name'
r = requests.get(url, headers = headers, params=params)
data = r.json()
print(data)