#!/usr/bin/env python
# -*- coding:utf-8 -*-

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

    with open('cookies.txt', 'r') as f:
        # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
        cookies_list = json.load(f)

        for cookie in cookies_list:
            # 该字段有问题所以删除就可以
            if 'expiry' in cookie:
                del cookie['expiry']
            # print(cookie)
            driver.add_cookie(cookie)

    driver.get('https://workflow.sues.edu.cn/default/work/shgcd/jkxxcj/jkxxcj.jsp')
    driver.refresh()
    sleep(3)

    # driver.find_element_by_xpath('//*[@id="form"]/div[10]/div/div/div[2]/div/div/label[1]/div/ins').click() # 留校
    # driver.find_element_by_xpath('//*[@id="form"]/div[10]/div/div/div[2]/div/div/label[2]/div/ins').click() # 在沪
    # driver.find_element_by_xpath('//*[@id="form"]/div[10]/div/div/div[2]/div/div/label[5]/div/ins').click()  # 其他地区

    driver.find_element_by_xpath('//*[@id="post"]').click() # 提交
    sleep(3)
    # driver.close()
    # driver.quit()
    #061520226
    #aA20020824