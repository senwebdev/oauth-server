import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.amazon.com/Intel-Ethernet-Adapter-I340-T4-packaging/dp/B003A7LKOU/ref=nav_signin?s=pc&ie=UTF8&qid=1538555515&sr=1-4&keywords=intel+ethernet+server+adapter&dpID=41mYieVJxwL&preST=_SY300_QL70_&dpSrc=srch&&')

soup = BeautifulSoup(response.text, 'html.parser')

a_page = soup.find(id='priceblock_ourprice')

print(soup.body)