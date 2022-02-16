import datetime
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # driver = webdriver.Chrome(executable_path=(r'/usr/bin/chromedriver'), options=chrome_options)
    driver = webdriver.Chrome(executable_path=(r'./chromedriver'))
    driver.get('https://workflow.sues.edu.cn')

    sleep(30)
    # c = driver.get_cookie('JSESSIONID')
    # print(c)
    with open('cookies.txt', 'w') as f:
        # 将cookies保存为json格式
        f.write(json.dumps(driver.get_cookies()))
    driver.close()
    driver.quit()
    #061520226
    #aA20020824