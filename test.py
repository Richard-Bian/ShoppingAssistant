# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 00:30
@Auth ： 边圣陶
@File ：test.py
@IDE ：PyCharm
@Email ：bian.shengtao@gmail.com
"""
import time

from selenium import webdriver


chromedriver_dir = '/Users/bianshengtao/Project/github/ShoppingAssistant/webdriver/chromedriver_mac_arm6/chromedriver'
driver = webdriver.Chrome(chromedriver_dir)  # Optional argument, if not specified will search path.

driver.get('https://www.jd.com/');


# 打印出页面的标题
print(driver.title)

# 关闭浏览器
driver.quit()
