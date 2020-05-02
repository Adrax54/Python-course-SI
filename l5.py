import requests
import time

def bitbay_BTC_ticker():
    response = requests.get('https://bitbay.net/API/Public/BTC/ticker.json')

    return response.json()

def bitbay_ETH_ticker():
    response = requests.get('https://bitbay.net/API/Public/ETH/ticker.json')
    return response.json()

def bitbay_LSK_ticker():

    response = requests.get('https://bitbay.net/API/Public/LSK/ticker.json')
    return response.json()

def bitbay_LTC_ticker():
    response = requests.get('https://bitbay.net/API/Public/LTC/ticker.json')
    return response.json()

def bitbay_GAME_ticker():
    response = requests.get('https://bitbay.net/API/Public/GAME/ticker.json')
    return response.json()

def profit():

  eth = bitbay_ETH_ticker()
  ticker = bitbay_BTC_ticker()
  lsk = bitbay_LSK_ticker()
  ltc = bitbay_LTC_ticker()
  game = bitbay_GAME_ticker()

  btc_values = [ticker['max'], ticker['min']]
  eth_values = [eth['max'], eth['min']]
  lsk_values = [lsk['max'], lsk['min']]
  ltc_values = [ltc['max'], ltc['min']]
  game_values = [game['max'], game['min']]

  values = {'btc': btc_values, 'eth': eth_values, 'lsk': lsk_values, 'ltc': ltc_values, 'game': game_values}

  list_of_percents = {}

  for key,value in values.items():
      sub = values[key]
      percent = ((sub[1]-sub[0])/sub[0]) * 100
      list_of_percents[key] = percent

  list_for_printing = {}

  for i in range(len(list_of_percents)):

      max_variable = max(list_of_percents.values())
      max_variable_key = max(list_of_percents, key = list_of_percents.get)
      list_for_printing[max_variable_key] = max_variable

      del list_of_percents[max_variable_key]

  for key,value in list_for_printing.items():

      print(key,':', value, '%')

five_minutes = 300

while True:

    profit()
    time.sleep(five_minutes)



