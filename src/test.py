import tkinter as tk
from okex_websocket import price_dict, main

m = main()


def refreshText():
    for i in range(len(price_dict.keys())):
        globals()[list(price_dict.keys())[i] + 'price']['text'] = next(m)[list(price_dict.keys())[i]]
    windows.after(100, refreshText)


windows = tk.Tk()
windows.geometry('500x500')  ## 规定窗口大小500*500像素

for i in range(len(price_dict.keys())):
    # print(price_dict.keys())
    globals()[list(price_dict.keys())[i]] = tk.Label(windows, text=list(price_dict.keys())[i]+':', font=("宋体", 10))
    globals()[list(price_dict.keys())[i]].grid(row=i, column=0)
    globals()[list(price_dict.keys())[i] + 'price'] = tk.Label(windows, text=next(m)[list(price_dict.keys())[i]], font=("宋体", 10))
    globals()[list(price_dict.keys())[i] + 'price'].grid(row=i, column=1)

# label_btc = tk.Label(windows, text="BTC-USTD:", font=("宋体", 10))
# label_btc.grid(row=0, column=1)
# label_btc_price = tk.Label(windows, text=next(m)['BTC-USDT'], font=("宋体", 10))
# label_btc_price.grid(row=1, column=1)

# label_eth = tk.Label(windows, text="ETH-USTD:", font=("宋体", 10))
# label_eth.grid(row=2, column=1)
# label_eth_price = tk.Label(windows, text=next(m)['ETH-USDT'], font=("宋体", 10))
# label_eth_price.grid(row=3, column=1)


windows.after(100, refreshText)
windows.mainloop()
