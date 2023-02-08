import requests
import datetime
import time

from bs4 import BeautifulSoup as bs

def get_datetime():
    current_time = datetime.datetime.now()
    nice_print_time = str(current_time.strftime('%d-%m-%Y %H:%M'))
    return nice_print_time

nice_print_time = get_datetime()

# s = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol=XRPBUSD')
# data = s.json()
# current_price  = data['price']
# print(f'Time: {nice_print_time}\nXRP rate: $ {current_price}')
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

current_price = get_current_price()

print(f'Time: {nice_print_time}\nXRP rate: $ {current_price}')

while True:
    get_current_price()
    history[count] = current_price

    if max(history)/current_price * 100 - 100 >= 1:
        print(f'Time: {nice_print_time}\nXRP rate: {current_price}')

    count = (count + 1) % sec_in_hour
    time.sleep(1)