import requests
import os
import json
# url = "https://swapi.dev/api/people/1/"

# response = requests.get(url )
# print(response.status_code)
# # print(response.json())
# import json
# dpla_data = response.json()
# with open('SW.json', 'w') as f:
#     json.dump(dpla_data, f)

people_data = []

for i in range(1, 84):
    url = f"https://swapi.dev/api/people/{i}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        people_data.append(data)
    else:
        print(f"Request for person {i} failed with status code {response.status_code}")

with open('SW_people.json', 'w') as f:
    json.dump(people_data, f,indent=2)