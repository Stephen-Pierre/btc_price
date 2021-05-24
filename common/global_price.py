from src import okex_websocket
import json


btc_usdt = okex_websocket.subscribe_okex_btc_usdt()
eth_usdt = okex_websocket.subscribe_okex_eth_usdt()
okb_usdt = okex_websocket.subscribe_okex_okb_usdt()


def process_okex_btc_value():
    global btc_usdt
    try:
        price = json.loads(next(btc_usdt))['data'][0]['last']
        return price
    except KeyError:
        return 'loading'


def process_okex_eth_value():
    global eth_usdt
    try:
        price = json.loads(next(eth_usdt))['data'][0]['last']
        return price
    except KeyError:
        return 'loading'


def process_okex_okb_value():
    global eth_usdt
    try:
        price = json.loads(next(okb_usdt))['data'][0]['last']
        return price
    except KeyError:
        return 'loading'