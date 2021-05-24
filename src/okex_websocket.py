import time
import queue
import websocket
import json


def subscribe_okex_btc_usdt():
    msg = {
        "op": "subscribe",
        "args": [
            {
                "channel": "tickers",
                "instId": "BTC-USDT"
            },
        ]
    }

    ws = websocket.create_connection('wss://ws.okex.com:8443/ws/v5/public')
    ws.send(json.dumps(msg))
    while True:
        yield ws.recv()


def subscribe_okex_eth_usdt():
    msg = {
        "op": "subscribe",
        "args": [
            {
                "channel": "tickers",
                "instId": "ETH-USDT"
            }
        ]
    }

    ws = websocket.create_connection('wss://ws.okex.com:8443/ws/v5/public')
    ws.send(json.dumps(msg))
    while True:
        yield ws.recv()


def subscribe_okex_okb_usdt():
    msg = {
        "op": "subscribe",
        "args": [
            {
                "channel": "tickers",
                "instId": "OKB-USDT"
            }
        ]
    }

    ws = websocket.create_connection('wss://ws.okex.com:8443/ws/v5/public')
    ws.send(json.dumps(msg))
    while True:
        yield ws.recv()

price_dict = {
    'BTC-USDT': 'loading',
    'ETH-USDT': 'loading',
    'DOGE-USDT': 'loading',
    'ADA-USDT': 'loading',
    'XRP-USDT': 'loading',
    'USDT-USDK': 'loading',
    'DOT-USDT': 'loading',
    'ICP-USDT': 'loading',
    'BCH-USDT': 'loading',
    'LTC-USDT': 'loading',
    'LINK-USDT': 'loading',
    'XLM-USDT': 'loading',
    'ETC-USDT': 'loading',
    'THETA-USDT': 'loading',
    'MATIC-USDT': 'loading',
    'TRX-USDT': 'loading',
    'UNI-USDT': 'loading',
    'EOS-USDT': 'loading',
    'FIL-USDT': 'loading',
    'SHIB-USDT': 'loading',
    'USDC-USDT': 'loading',
    'XMR-USDT': 'loading',
    'OKB-USDT': 'loading',
    'NEO-USDT': 'loading',
    'AAVE-USDT': 'loading',
    'BSV-USDT': 'loading',
    'ALGO-USDT': 'loading',
    'KSM-USDT': 'loading',
    'LEO-USDT': 'loading',
    'CEL-USDT': 'loading',
    'ATOM-USDT': 'loading',
    'IOTA-USDT': 'loading',
    'CRO-USDT': 'loading',
    'XTZ-USDT': 'loading',
    'BTT-USDT': 'loading',
    'LUNA-USDT': 'loading',
    'WBTC-USDT': 'loading',
    'MKR-USDT': 'loading',
    'KLAY-USDT': 'loading',
    'XEM-USDT': 'loading',
    'DASH-USDT': 'loading',
    'WAVES-USDT': 'loading',
    'COMP-USDT': 'loading',
    'SNX-USDT': 'loading',
    'ZEC-USDT': 'loading',
    'DCR-USDT': 'loading',
    'HBAR-USDT': 'loading',
    'CHZ-USDT': 'loading',
    'EGLD-USDT': 'loading',
    'DAI-USDT': 'loading',
    'SUSHI-USDT': 'loading',
    'ZIL-USDT': 'loading',
    'SOL-USDT': 'loading',
    'YFI-USDT': 'loading',
    'ENJ-USDT': 'loading',
    'BTG-USDT': 'loading',
    'QTUM-USDT': 'loading',
    'BAT-USDT': 'loading',
    'MANA-USDT': 'loading',
    'DGB-USDT': 'loading',
    'ZEN-USDT': 'loading',
    'STX-USDT': 'loading',
    'GRT-USDT': 'loading',
    'ONT-USDT': 'loading',
    'NANO-USDT': 'loading',
    'OKT-USDT': 'loading',
    'SC-USDT': 'loading',
    'UMA-USDT': 'loading',
    'OMG-USDT': 'loading',
    'ZRX-USDT': 'loading',
    'ICX-USDT': 'loading',
    'NEAR-USDT': 'loading',
    'KISHU-USDT': 'loading',
    'CTC-USDT': 'loading',
    'RVN-USDT': 'loading',
    'BCD-USDT': 'loading',
    'ANC-USDT': 'loading',
    'CELO-USDT': 'loading',
    'LSK-USDT': 'loading',
    'IOST-USDT': 'loading',
    'FTM-USDT': 'loading',
    'PAX-USDT': 'loading',
    'AVAX-USDT': 'loading',
    'LRC-USDT': 'loading',
    'XCH-USDT': 'loading',
    'SUN-USDT': 'loading',
    'LPT-USDT': 'loading',
    'REN-USDT': 'loading',
    'KNC-USDT': 'loading',
    'BCHA-USDT': 'loading',
    'TUSD-USDT': 'loading',
    'SNT-USDT': 'loading',
    'FLOW-USDT': 'loading',
    'RSR-USDT': 'loading',
    'GLM-USDT': 'loading',
    'BNT-USDT': 'loading',
    'AKITA-USDT': 'loading',
    'CFX-USDT': 'loading',
    'MCO-USDT': 'loading',
    'ARDR-USDT': 'loading',
}

def subscribe_all():
    msg = {
        "op": "subscribe",
        "args": [{"channel": "tickers", "instId": x} for x in price_dict.keys()]
    }
    print(msg)

    ws = websocket.create_connection('wss://ws.okex.com:8443/ws/v5/public')
    ws.send(json.dumps(msg))
    while True:
        yield ws.recv()





def main():
    res = subscribe_all()
    while True:
        # for i in range(6):
        response = json.loads(next(res))
        try:
            price_dict[response['data'][0]['instId']] = response['data'][0]['last']
            yield price_dict
        except KeyError:
            pass
        # time.sleep(2)


q = queue.Queue()


def generate_queue():
    res = subscribe_all()
    while True:
        response = json.loads(next(res))
        try:
            price_dict[response['data'][0]['instId']] = response['data'][0]['last']
            q.put(price_dict)
            print(q.get())
        except KeyError:
            pass


if __name__ == '__main__':
    main()
