import requests


def bitbay_data():

    response = requests.get("https://bitbay.net/API/Public/BTC/orderbook.json")

    return response.json()

def bitbay_data_ticker():

    response = requests.get('https://bitbay.net/API/Public/BTC/ticker.json')

    return response.json()

def get_trading_data():
    
    response = requests.get('https://blockchain.info/ticker')

    return response.json()

Trade = get_trading_data()
ticker = bitbay_data_ticker()
orderbook_bitbay = bitbay_data()


ASKS_bitbay = orderbook_bitbay['asks']
BIDS_bitbay = orderbook_bitbay['bids']

buy_trading = Trade['USD']['buy']
sell_trading = Trade['USD']['sell']

Ticker_bitbay_buy = ticker['ask']
ticker_bitbay_sell = ticker['bid']


print('first ten offers from bitbay\n')
print('SALE PRICE:')
for i in ASKS_bitbay[:10]:
    print(i,'\n')
print('BUY PRICE:')
for i in BIDS_bitbay[:10]:
    print(i,'\n')


if buy_trading < Ticker_bitbay_buy:
    print('Its better to buy BTC from blockchain for price',buy_trading,'USD')
else:
    print('Its better to buy BTC from bitbay for price',Ticker_bitbay_buy,'USD')

if sell_trading > ticker_bitbay_sell :
    print('Its better to sell on BTC blockchain for',sell_trading,'USD')
else:
    print('Its better to sell on BTC Bitbay for',ticker_bitbay_sell,'USD')




