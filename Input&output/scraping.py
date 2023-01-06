import openpyxl
import requests
from bs4 import BeautifulSoup

try:
    response = requests.get("https://vegetablemarketprice.com/market/tamilNadu/history")
    soup = BeautifulSoup(response.text ,'html.parser')
    print(soup)
except Exception as e:
    print(e)
