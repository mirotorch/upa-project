import requests
from bs4 import BeautifulSoup
"""
Get the URLs of the products and write them into stdout
"""
# first & second page (200 products in total)
pages_urls = [ 'https://www.digikey.cz/en/products/filter/vestav%C4%9Bn%C3%BD/mikrokontrol%C3%A9ry/685?s=N4IgrCBcoA5QjAGhDOl4AYMF9tA',
               'https://www.digikey.cz/en/products/filter/vestav%C4%9Bn%C3%BD/mikrokontrol%C3%A9ry/685?s=N4IgrCBcoA5QTAGhDOkCMAGTBfHQ'] 
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0'}

href_class  = 'tss-css-41s5xv-productColExpandedPartNumber-anchor'

for page in pages_urls:
    response = requests.get(page, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = soup.find_all('a', class_=href_class)
    for url in urls:
        print('https://www.digikey.cz' + url['href'])