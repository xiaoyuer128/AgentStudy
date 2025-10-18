"""
作者：Zxy
"""
from operator import itemgetter
import langchain
#开启调试模式
langchain.debug = True
import os
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, SystemMessagePromptTemplate, \
    HumanMessagePromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableLambda
from langchain_openai import ChatOpenAI
from langserve import add_routes
from fastapi import FastAPI
from langchain_core.runnables import chain

MODEL_API_KEY = os.getenv("DASHSCOPE_API_KEY")
#拿到一个访问大模型的客户端
client = ChatOpenAI(api_key=MODEL_API_KEY,
                    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
                    model="qwen-max-latest"
                    )


chat_template = ChatPromptTemplate.from_template("{a}+{b}是多少")
#获取字符串长度
def length_function(text):
    return len(text)
#将两个字符串长度相乘
def _multiple_length_function(text1,text2):
    return len(text1) * len(text2)
#创建一个函数，将两个字符串长度相乘
@chain
def multiple_length_function(_dict):
    return _multiple_length_function(
        _dict["text1"],
        _dict["text2"]
    )

chain1 = chat_template | client
chain2 = (
        {
            "a":itemgetter("foo") | RunnableLambda(length_function),
            "b":{"text1":itemgetter("foo"),"text2":itemgetter("bar")}| multiple_length_function
        }
    | chain1)
print(chain2.invoke({"foo":"abc","bar":"abcd"}))