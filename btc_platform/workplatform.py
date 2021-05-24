import tkinter as tk
from src import okex_websocket

ws = okex_websocket.subscribe()


def update_value():
    global ws
    label_2['text'] = next(ws)
    top.after(1000, update_value())


top = tk.Tk()
top.title('BTC-index')
top.geometry('1200x600')
label_1 = tk.Label(top, text='BTC-USTD:', font=("宋体", 14))
label_1.grid(row=0, column=0)
print('here')
label_2 = tk.Label(top, text=next(ws), font=("宋体", 14))
label_2.grid(row=0, column=1)

top.after(1000, update_value())

top.mainloop()


# if __name__ == '__main__':

    # t = threading.Thread(target=okex_websocket.subscribe())
    # t.daemon = True
    # t.start()
    # m = threading.Thread(target=main())
    # m.start()
    # main()
