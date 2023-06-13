# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/17 19:10
@Auth ： 边圣陶
@File ：page.py
@IDE ：PyCharm
@Email ：bian.shengtao@gmail.com
"""
import gradio as gr
import openai
from config import *
from accurate_search import search
import json
openai.api_key = OPENAI_API_KEY
messages = [
    {"role": "system", "content": f"{prompt}"},
]
def chat_with_gpt3(prompt):
    messages.append({"role": "user", "content": prompt})
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    response = completion.choices[0].message["content"]
    messages.append({"role": "assistant", "content": response})
    print(response)
    recommendation = json.loads(response)["recommendation"]
    message = ""
    for product in recommendation.values():
        res = search(product)
        message += f"## {res}\n"
    messages.append({"role": "user", "content": f"{message}"})
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return completion.choices[0].message["content"]
iface = gr.Interface(fn=chat_with_gpt3, inputs="text", outputs="text")
iface.launch()

