import requests
from bs4 import BeautifulSoup


url = "https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
response = requests.get(url, headers=headers)
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())  # prints well-formatted HTML