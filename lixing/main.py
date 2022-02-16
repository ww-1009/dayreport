#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

from Driver import driver

if __name__ == '__main__':
    user="201340226"
    pwd="Ww20011009"
    province="浙江省"
    city="宁波市"
    region="江东区"
    inschool=0

    while True:
        driver = driver()
        driver.run(user=user,pwd=pwd,province=province,city=city,region=region,inSchool=inschool)





