import requests
import os


# dpla_api_key = os.environ['DPLA_API_KEY']
# print(dpla_api_key)
import apikey

# apikey.save("dpla_key", api_key)

dpla_api_key = apikey.load("dpla_key")



dpla_api_key = apikey.load("dpla_key")
url = 'https://api.dp.la/v2/items?q=kittens&api_key='

response = requests.get(url + dpla_api_key)
print(response.status_code)
# print(response.json())
import json
dpla_data = response.json()
with open('dpla_kittens.json', 'w') as f:
    json.dump(dpla_data, f)

# print(dpla_data.keys())

# print('dataProvider', dpla_data['docs'][0]['dataProvider'])

# print('isShownAt', dpla_data['docs'][0]['isShownAt'])

# print('sourceResource', dpla_data['docs'][0]['sourceResource'])
# print('object', dpla_data['docs'][0]['object'])

from dpla.api import DPLA
dpla = DPLA(dpla_api_key)

# Now make your search
response = dpla.search(q="kittens")
print(response.items[0])