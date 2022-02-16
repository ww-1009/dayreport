#!/usr/bin/python3

import datetime
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')

    with open('/home/project/test.txt', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        num=5
        line1 = line.rstrip().split()
        user = line1[0]
        pwd = line1[1]
        province = line1[2]
        city = line1[3]
        region = line1[4]
        inSchool = int(line1[5])
        name = line1[6]
        while num:
            try:
                driver = webdriver.Chrome(executable_path=(r'/usr/bin/chromedriver'), options=chrome_options)
                driver.get('https://cas.paas.lixin.edu.cn/dist/')
                sleep(2)
                driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[6]/span/a').click()
                driver.find_element_by_xpath(
                    '// *[ @ id = "app"] / div / div[1] / div[3] / div[2] / div[2] / div[1] / div[1] / ul / li[2]').click()
                sleep(2)
                driver.switch_to.window(driver.window_handles[1])
                username = driver.find_element_by_xpath('//*[@id="username"]')
                username.send_keys(user)
                password = driver.find_element_by_xpath('//*[@id="password"]')
                password.send_keys(pwd)
                sleep(1)
                driver.find_element_by_xpath('//*[@id="fm1"]/div[4]/div/input[5]').click()
                sleep(2)
                # 新建报告
                driver.find_element_by_xpath('//*[@id="dw_nBtn"]').click()
                sleep(2)
                driver.switch_to.frame('dw_mobile_target_frame')
                # 点击居住地下拉箭头
                driver.find_element_by_xpath('//*[@id="table_container"]/tbody[1]/tr[8]/td[2]/span/div/span/span').click()
                sleep(2)
                if province != "上海市":
                    s0 = driver.find_element_by_xpath('//*[@id="radioActionSheetContent"]/li[3]/span')
                    driver.execute_script("arguments[0].click();", s0)
                    s1 = Select(driver.find_element_by_id("selProvince_SF"))  # 实例化Select
                    sleep(2)
                    s1.select_by_visible_text(province)
                else:
                    s0 = driver.find_element_by_xpath('//*[@id="radioActionSheetContent"]/li[2]/span')
                    driver.execute_script("arguments[0].click();", s0)
                sleep(2)
                s2 = Select(driver.find_element_by_id("selCity_SF"))  # 实例化Select
                sleep(2)
                s2.select_by_visible_text(city)
                s3 = Select(driver.find_element_by_id("selArea_SF"))
                sleep(2)
                s3.select_by_visible_text(region)
                # 定位到下拉选择框
                driver.find_element_by_xpath(
                    '/html/body/form/div/table/tbody/tr[2]/td/table/tbody[1]/tr[13]/td[2]/span/div/span/span').click()
                sleep(2)
                if inSchool:
                    # 在校时体温正常
                    driver.find_element_by_xpath('// *[ @ id = "comboBoxActionSheetContent"] / li[2] / span').click()  # 在校
                    driver.find_element_by_xpath(
                        '//*[@id="XW"]/td[2]/span/div/span/span').click()
                    sleep(2)
                    driver.find_element_by_xpath('//*[@id="comboBoxActionSheetContent"]/li[3]/span').click()  #
                else:
                    driver.find_element_by_xpath('//*[@id="comboBoxActionSheetContent"]/li[3]/span').click()  # 不在校
                    sleep(1)

                driver.find_element_by_xpath('//*[@id="BTN_SAVE"]').click()
                sleep(2)
                time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(time+name+"提交成功")
                driver.close()
                driver.quit()
                break
            except Exception as e:
                num=num-1
                print(e)
                sleep(5)
