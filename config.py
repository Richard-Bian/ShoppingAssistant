# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/15 01:20
@Auth ： 边圣陶
@File ：config.py
@IDE ：PyCharm
@Email ：bian.shengtao@gmail.com
"""
# your username
YOUR_USERNAME = "your_username"

# your password
YOUR_PASSWORD = "your_password"

# chromedriver path
CHROME_DRIVER_PATH = "path/to/your/chromedriver"

# openai api key
OPENAI_API_KEY = "sk-your_api_key"

prompt = '''
你是一个商城导购员，仿照下面例子，给我推荐一些合适的东西。输入：我喜欢跑步。以下格式生成推荐商品的json格式的请求
{
  "input": "我喜欢跑步",
  "recommendation": {
    "product1": "跑鞋“,
  “product2”:"跑步运动服"
  }
}，只需要返回代码，不需要任何文字性描述。之后我会将你返回的代码通过我的接口查询商品，并返回商品名和商品链接，你需要依据你之前所分解需求的商品和我所给的信息，生成markdown格式的购物清单
'''