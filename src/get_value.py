from okex_websocket import q, generate_queue
import threading

t = threading.Thread(target=generate_queue())
t.setDaemon()
t.start()


while not q.empty():
    val = q.get()
    print(val)