import requests
import threading

def bitstamp_ticker():
    response = requests.get('https://www.bitstamp.net/api/ticker/')
    return response.json()

def bitbay_data_ticker():

    response = requests.get('https://bitbay.net/API/Public/BTC/ticker.json')

    return response.json()

def get_coinbase_buy_data_ticker():

    response_buy = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy.json')

    return response_buy.json()

def get_coinbase_sell_data_ticker():
    response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell.json')
    return response.json()

def get_blockchain_ticker():
    response = requests.get('https://blockchain.info/ticker')
    return response.json()

wallet = [0,0.03]

def Arbitrage(wallet):

    bitstamp = bitstamp_ticker()
    bitbay = bitbay_data_ticker()
    coinbasesell = get_coinbase_sell_data_ticker()
    coinbasebuy = get_coinbase_buy_data_ticker()
    blockchain = get_blockchain_ticker()

    bitstamp_bit = float(bitstamp['bid'])

    bitstamp_ask = float(bitstamp['ask'])

    bitbay_bid = float(bitbay['bid'])

    bitbay_ask = float(bitbay['ask'])

    coinbase_sell = float(coinbasesell['data']['amount'])

    coinbase_buy = float(coinbasebuy['data']['amount'])

    blockchain_buy = float(blockchain['USD']['buy'])

    blockchain_sell = float(blockchain['USD']['sell'])


    buy_index = {'bitbay':bitbay_ask, 'bitstamp':bitstamp_ask, 'coinbase':coinbase_buy, 'blockchain':blockchain_buy}


    sell_index = {'bitbay':bitbay_bid, 'bitstamp':bitstamp_bit, 'coinbase':coinbase_sell, 'blockchain':blockchain_sell}

    Taker_index = {'bitbay':0.0043 ,'bitstamp':0.005 , 'coinbase':0.005 , 'blockchain':0.024}

    lowest_price_to_buy = min(buy_index.values())
    lowest_price_to_buy_key = min(buy_index, key= buy_index.get)

    highiest_price_to_sell = max(sell_index.values())
    highiest_price_to_sell_key = max(sell_index, key = sell_index.get)

    Taker_index_buy = Taker_index[lowest_price_to_buy_key]
    Taker_index_sell = Taker_index[highiest_price_to_sell_key]

    myusd = wallet[0]
    mybtc = wallet[1]
    arbitrage_buy = mybtc *lowest_price_to_buy * (1+Taker_index_buy)
    arbitrage_sell = mybtc * highiest_price_to_sell *(1-Taker_index_sell)

    if arbitrage_buy < arbitrage_sell:
        print('You can buy',mybtc,'bitcoin on :',lowest_price_to_buy_key,'for',lowest_price_to_buy, '\n and sell on:', highiest_price_to_sell_key,'for',
              highiest_price_to_sell, '\n with profit:', round((arbitrage_sell - arbitrage_buy),3),'USD')
        income  = arbitrage_sell - arbitrage_buy #USD
        condition = income + mybtc
        if condition > mybtc:
            wallet[0] = arbitrage_sell
            wallet[1] = 0
            buy = wallet[0] / lowest_price_to_buy
            wallet[0] = 0
            wallet[1] = buy
            print('wallet [USD, BTC] : ->>>>>>',wallet)
        else : print('We wont make any profit if we buy right now')
    else: print('not worth buying',wallet,'\n','BUY PRICE:',arbitrage_buy,lowest_price_to_buy_key, "\nSELL PRICE:",arbitrage_sell,highiest_price_to_sell_key)

    threading.Timer(5, Arbitrage(wallet)).start()

Arbitrage(wallet)
