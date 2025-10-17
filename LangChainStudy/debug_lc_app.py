"""
作者：Zxy
"""
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, SystemMessagePromptTemplate, \
    HumanMessagePromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from langserve import add_routes
from fastapi import FastAPI
import langchain
#开启调试模式
langchain.debug = True
#获取apikey
MODEL_API_KEY = os.getenv("DASHSCOPE_API_KEY")
#拿到一个访问大模型的客户端
client = ChatOpenAI(api_key=MODEL_API_KEY,
                    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
                    model="qwen-max-latest"
                    )

text1 = "此情可待成追忆。只是当时已惘然"
text = '你是一名大学的翻译老师，对于下列诗句进行"{language}"翻译'

#聊天模型:接收消息列表
chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(text),
        HumanMessagePromptTemplate.from_template("{text2}")
    ]
)

parser = StrOutputParser ()

chain = chat_template | client | parser#管道操作符“|”
# chain = RunnableSequence(chat_template, client, parser)#等价于上面


# chain.invoke({'language': '英语', 'text2':text1})
app = FastAPI(title = '翻译大模型服务',
                version = '0.0.1',
                description = '基于langchain的翻译大模型服务'
               )
# add_routes(app, chain, path = '/tslServer')

add_routes(app, chain, path = '/tslServer')
if __name__ == '__main__':
        import uvicorn
        uvicorn.run(app, host = 'localhost', port = 0)