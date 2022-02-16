#!/usr/bin/env python
# -*- coding:utf-8 -*-

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium import webdriver


class driver():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        # self.driver = webdriver.Chrome(options=option)

    def run(self, user, pwd, province, city, region, inSchool):
        self.driver.get('https://cas.paas.lixin.edu.cn/dist/')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[6]/span/a').click()
        self.driver.find_element_by_xpath(
            '// *[ @ id = "app"] / div / div[1] / div[3] / div[2] / div[2] / div[1] / div[1] / ul / li[2]').click()
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        # u = "201340226"
        # p = "Ww20011009"
        username = self.driver.find_element_by_xpath('//*[@id="username"]')
        username.send_keys(user)
        password = self.driver.find_element_by_xpath('//*[@id="password"]')
        password.send_keys(pwd)
        self.driver.find_element_by_xpath('//*[@id="fm1"]/div[4]/div/input[5]').click()
        print("登入成功！")
        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="dw_nBtn"]').click()
        print("新建")
        self.driver.switch_to.frame('side_dw_m_page_frame')
        sleep(1)
        if province != "上海市":
            self.driver.find_element_by_xpath(
                '//*[@id="aws-form-formcontent"]/td/table[1]/tbody[3]/tr[2]/td[2]/span/table/tbody/tr/td[2]/div/ins').click()
            s1 = Select(self.driver.find_element_by_id("selProvince_SF"))  # 实例化Select
            sleep(2)
            s1.select_by_visible_text(province)
            print(province)
        else:
            self.driver.find_element_by_xpath(
                '//*[@id="DQJZS_Tip"]/div/ins').click()
            sleep(2)
        s2 = Select(self.driver.find_element_by_id("selCity_SF"))  # 实例化Select
        sleep(2)
        s2.select_by_visible_text(city)
        print(city)
        s3 = Select(self.driver.find_element_by_id("selArea_SF"))
        sleep(2)
        s3.select_by_visible_text(region)
        print(region)
        # 定位到下拉选择框
        self.driver.find_element_by_xpath('//*[@id="select2-SFZX-container"]/span').click()
        s4 = self.driver.find_element_by_id("select2-SFZX-container")
        if inSchool:
            # 在校时体温正常
            s4.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[1]').click()  # 在校
            self.driver.find_element_by_xpath(
                '//*[@id="c8e3389c_6c90_0001_d85d_17d681701bd3"]/td[2]/span/span/span[1]/span/span[2]').click()
            print("在校")
            s5 = self.driver.find_element_by_id("select2-XW_XWTW-container")
            s5.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()  # 正常体温
            print("体温正常")
        else:
            s4.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()  # 不在校
            print("不在校")

        # self.driver.find_element_by_xpath('//*[@id="BTN_SAVE"]').click()
        sleep(2)
        print("提交成功")
        self.driver.close()
        self.driver.quit()

