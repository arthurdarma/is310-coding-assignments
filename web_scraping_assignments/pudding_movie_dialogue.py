import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup
# edited1
df = pd.read_csv('cleaned_pudding_data.csv')
links = df['link']
with open('pudding_movie_dialogue.csv', 'w') as file:
     writer = csv.writer(file)
     writer.writerow(['Link', 'Script'])
     for i in links:
            response = requests.get(i)
            if response.status_code != 200:
                        continue
            soup = BeautifulSoup(response.text, "html.parser")
            writer.writerow([ i, soup.get_text()[:1000]])

