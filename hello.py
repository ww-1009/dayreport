#!/usr/bin/python3

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path=(r'./chromedriver'), options=chrome_options)
# driver = webdriver.Chrome(executable_path=(r'./chromedriver'))
driver.implicitly_wait(30)
baseURL='https://baike.baidu.com/item/'
print("查询对象")
inputStr=input()
driver.get(baseURL+inputStr)

url = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/a/img').get_attribute('src')
driver.quit()
print(url)
# 通过requests发送一个get请求到图片地址，返回的响应就是图片内容
# r = requests.get(url)
#
# # 将获取到的图片二进制流写入本地文件
# with open('baidu.png', 'wb') as f:
#     # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
#     f.write(r.content)

