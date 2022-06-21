import requests
import json
import time
import datetime

from filemanagement import *

key = getFromConfig('api_url')+getFromConfig('typeofcrypto')
print(key)
print(getFromConfig('difference'))

old_data = {'symbol': 'BTCEUR', 'price': '0'}

while True:

    currentDate = datetime.datetime.now()
    date = {'year': currentDate.year,
            'month': currentDate.month,
            'day': currentDate.day,
            'hour': currentDate.hour,
            'minute': currentDate.minute,
            'second': currentDate.second
            }

    data = requests.get(key)  
    data = data.json()

    date["btceurprice"] = data['price']

    print(str(data['price']) + " <- btc price "+ str(old_data['price'] + " <- old btc price"))

    if float(data['price']) - float(old_data['price']) >= float(getFromConfig('difference')) or float(data['price']) - float(old_data['price']) <= (float(getFromConfig('difference')) * -1):
        print(f"{data['symbol']} price is {data['price']}")
        writeFile(getFromConfig('dataFile'), str(date))

        old_data = data.copy()

    time.sleep(1)