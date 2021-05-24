import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_now_price():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/73.0.3679.0 Safari/537.36',
        'Connection': 'close'
        }
    url = 'http://www.okex.com/api/index/v5/BTC-USD/constituents'
    response = requests.get(url=url, headers=headers)
    content = json.loads(response.text)
    # print(content)
    price = content['data']['last']
    print(price)


def get_now_price_by_selenium():
    url = 'https://www.okex.com/markets/prices'
    attr = 'last-num'
    browser = webdriver.Chrome()
    browser.get(url)
    WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, attr))
    )
    while True:
        price = browser.find_element_by_xpath("//div[@class='token-list']//tr//td//div[@class='last-num']")
        print(price.text)
        time.sleep(0.2)


if __name__ == '__main__':
    while True:
        get_now_price()
        time.sleep(0.01)
    # get_now_price_by_selenium()
