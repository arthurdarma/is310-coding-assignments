import bs4
# soup = bs4.BeautifulSoup(html_doc, 'html.parser')
# 'bs4' is the package, 'BeautifulSoup' is a class defined inside the package definition
print(bs4.__version__)
from bs4 import BeautifulSoup
# soup = BeautifulSoup(open("humanist_homepage.html"), features="html.parser")

# print(soup.prettify())

# links = soup.find_all('a')

# for link in links:
#     print(link.get_text())
import requests
response = requests.get("https://humanist.kdl.kcl.ac.uk/")

print(response.status_code)
print(response.headers)
soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify())
links = soup.find_all('a')

for link in links:
    if "Archives" in link.get('href'):
        print(link.get_text())
        volume_url = "https://humanist.kdl.kcl.ac.uk" + link.get('href')
        volume_response = requests.get(volume_url)
        volume_soup = BeautifulSoup(volume_response.text, "html.parser")
        print(volume_soup.get_text())
    
import csv

with open('humanist_volumes.csv', 'w') as file:
    writer = csv.writer(file)
    # Write the headers
    writer.writerow(['Link', 'Volume Text'])
    for link in links:
        if "Archives" in link.get('href'):
            volume_url = "https://humanist.kdl.kcl.ac.uk" + link.get('href')
            volume_response = requests.get(volume_url)
            volume_soup = BeautifulSoup(volume_response.text, "html.parser")
            writer.writerow([link.get_text(), volume_soup.get_text()])