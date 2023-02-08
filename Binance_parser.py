import requests
import datetime
import time

from bs4 import BeautifulSoup as bs

def get_datetime():
    current_time = datetime.datetime.now()
    nice_print_time = str(current_time.strftime('%d-%m-%Y %H:%M'))
    return nice_print_time

# s = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol=XRPBUSD')
# data = s.json()
# current_price  = data['price']
# print(f'Time: {get_datetime()}\nXRP rate: $ {current_price}')
    # API request (price less accurate)

URL = 'https://www.binance.com/ru/price/xrp'

history = [0] * 3600
count = 0
sec_in_hour = 3600

def get_current_price():
    response = requests.get(URL)
    soup = bs(response.text,'lxml')
    x = soup.find(class_="css-12ujz79")

    current_price = x.text 
    current_price = float(current_price[2:])

    return current_price

print(f'Time: {get_datetime()}\nXRP rate: $ {get_current_price()}')

while True:
    history[count] = get_current_price()

    if max(history)/get_current_price() * 100 - 100 >= 1:
        print(f'Time: {get_datetime()}\nXRP rate: {get_current_price()}')

    count = (count + 1) % sec_in_hour
    time.sleep(1)