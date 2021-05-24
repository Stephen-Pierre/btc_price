import threading
from src import okex_websocket
from btc_platform import workplatform
# from multiprocessing import Process


def main():
    # workplatform.main()
    threads = []
    thread_1 = threading.Thread(target=okex_websocket.subscribe())

    thread_2 = threading.Thread(target=workplatform.main())
    threads.append(thread_2)
    threads.append(thread_1)
    for thread in threads:
        thread.start()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
