"""
作者：Zxy
"""
import os

from langchain_openai import ChatOpenAI
from openai import base_url

#获取apikey
MODEL_API_KEY = os.getenv("DASHSCOPE_API_KEY")
#拿到一个访问大模型的客户端
client = ChatOpenAI(api_key=MODEL_API_KEY,
                    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
                    model="qwen-max-latest"
                    )
message = [
    ('system','你是一名大学翻译专业的大师，你需要将下列话翻译为英文'),
    ('human','此情可待成追忆，只是当时已惘然')
    #'This kind of feeling can be cast into a fond memory,
    # but at that time, I was already lost in it.'
]
result = client.invoke( message)#唤醒调用
print( result)


