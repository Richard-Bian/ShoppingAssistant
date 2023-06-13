# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/21 20:13
@Auth ： 边圣陶
@File ：search_logistics_information.py
@IDE ：PyCharm
@Email ：bian.shengtao@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
wait = WebDriverWait(driver, 10)

# 导航到京东主页
driver.get('https://www.jd.com')

# 点击登录按钮
login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '你好，请登录')))
login_button.click()

# 切换到登录iframe
driver.switch_to.frame('login_frame')

# 在登录页面中输入你的用户名和密码
username = driver.find_element(By.ID, YOUR_USERNAME)
password = driver.find_element(By.ID, YOUR_PASSWORD)
username.send_keys('你的用户名')
password.send_keys('你的密码')

# 点击登录
login_submit = driver.find_element(By.ID, 'login_submit')
login_submit.click()

# 切换回主页面
driver.switch_to.default_content()

# 登录后，导航到你的订单页面
driver.get('https://order.jd.com/center/list.action')

# 在订单页面中，搜索你的iPhone订单
order_search_box = driver.find_element(By.ID, 'trade-keywords')
order_search_box.send_keys('iPhone')
order_search_button = driver.find_element(By.CLASS_NAME, 'form-btn')
order_search_button.click()

# 检查订单的状态
order_status = driver.find_element(By.CSS_SELECTOR, '.status').text
print(order_status)

driver.quit()