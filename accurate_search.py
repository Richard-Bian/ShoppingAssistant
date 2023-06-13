# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 01:26
@Auth ： 边圣陶
@File ：accurate_search.py
@IDE ：PyCharm
@Email ：bian.shengtao@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from getpass import getpass
from config import *

search_query = "iphone14 256G"



def search(search_query):
    # 创建一个新的Chrome浏览器实例
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    # 让浏览器访问京东的主页
    driver.get('https://www.jd.com')

    # 等待页面加载完成
    wait = WebDriverWait(driver, 10)

    # 检查是否已经登录
    try:
        user_info = driver.find_element_by_class_name('nickname')
        print('已经登录，用户名：', user_info.text)
    except:
        print('未登录，正在尝试登录...')
        # 让浏览器访问商城的登录页面，这里以京东为例
        driver.get('https://passport.jd.com/new/login.aspx')

        # 等待页面加载完成
        wait = WebDriverWait(driver, 10)

        # 点击账户登录
        account_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-tab.login-tab-r')))
        account_login.click()

        # 输入用户名
        username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginname')))
        username.clear()
        username.send_keys(f'{YOUR_USERNAME}')  # 请将'your_username'替换为你的用户名

        # 输入密码
        password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#nloginpwd')))
        password.clear()
        password.send_keys(f"{YOUR_PASSWORD}")  # 使用getpass函数来安全地输入你的密码

        # 点击登录按钮
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginsubmit')))
        login_button.click()

        # 等待页面加载完成
        driver.implicitly_wait(30)
        print("已登陆")

    print(search_query)
    # 在搜索框中输入"YOUR QUERY"
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.ID, 'key')))
    search_box.clear()
    search_box.send_keys(search_query)

    # 点击搜索按钮
    wait = WebDriverWait(driver, 10)
    search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button')))
    search_button.click()

    # 等待搜索结果加载完成
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.gl-item')))

    # 获取商品元素
    wait = WebDriverWait(driver, 10)
    items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.gl-item')))
    item = items[1]

    # 获取网址
    url_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.p-img a')))
    url = url_element.get_attribute('href')
    print('网址：', url)

    # 获取商品名称
    wait = WebDriverWait(driver, 10)
    name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.p-name')))
    name = name_element.text
    print('商品名称：', name)

    # 获取价格
    wait = WebDriverWait(driver, 10)
    price_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.p-price')))
    price = price_element.text
    print('价格：', price)



    # 关闭浏览器
    driver.quit()
    return {
        'url': url,
        'name': name,
        'price': price
    }