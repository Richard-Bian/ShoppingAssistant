# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 01:26
@Auth ： 边圣陶
@File ：accurate_search..py
@IDE ：PyCharm
@Email ：bian.shengtao@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
from config import *

# 创建一个新的Chrome浏览器实例
driver = webdriver.Chrome(chromedriver_dir)

# 让浏览器访问京东的登录页面
driver.get('https://passport.jd.com/new/login.aspx')

# 等待页面加载完成
wait = WebDriverWait(driver, 10)

# 点击账户登录
account_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-tab.login-tab-r')))
account_login.click()

# 输入用户名
username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginname')))
username.clear()
username.send_keys(f'{your_username}')  # 请将'your_username'替换为你的用户名

# 输入密码
password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nloginpwd')))
password.clear()
password.send_keys(f"{your_password}")  # 使用getpass函数来安全地输入你的密码

# 点击登录按钮
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginsubmit')))
login_button.click()

# 等待页面加载完成
driver.implicitly_wait(10)

# 在搜索框中输入"iphone14 黑色"
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.ID, 'key')))
search_box.clear()
search_box.send_keys('iphone14 黑色')

# 点击搜索按钮
wait = WebDriverWait(driver, 10)
search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button')))
search_button.click()

# 等待搜索结果加载完成
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gl-item')))

# 获取第一个搜索结果的网址
wait = WebDriverWait(driver, 10)
first_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gl-item .p-img a')))
url = first_result.get_attribute('href')
print(url)

# 访问商品的网址
driver.get(url)

# 等待页面加载完成
wait.until(EC.presence_of_element_located((By.ID, 'InitCartUrl')))

# 点击"加入购物车"按钮
wait = WebDriverWait(driver, 10)
add_to_cart_button = wait.until(EC.presence_of_element_located((By.ID, 'InitCartUrl')))
add_to_cart_button.click()

# 关闭浏览器
driver.quit()
