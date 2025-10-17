"""
作者：Zxy
"""
import os


from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, SystemMessagePromptTemplate, \
    HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from openai import base_url

#获取apikey
MODEL_API_KEY = os.getenv("DASHSCOPE_API_KEY")
#拿到一个访问大模型的客户端
client = ChatOpenAI(api_key=MODEL_API_KEY,
                    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
                    model="qwen-max-latest"
                    )

template_str = '你是一名大学的翻译老师，\n对于诗句{text}进行翻译'
text1 = "此情可待成追忆。只是当时已惘然"
#方法：
# prompt  = PromptTemplate.from_template(template_str)
# prompt2 = PromptTemplate(
#     template=template_str,
#     input_variables=["text"]#变量需要显式的写出来
# )
# print(prompt.format(text=text1))
#  #调用
# print(client.invoke(prompt.format(text=text1)))

text = '你是一名大学的翻译老师，对于下列诗句进行"{language}"翻译'
#聊天模型:接收消息列表
chat_template = ChatPromptTemplate.from_messages(
    [
        # ('system',text),
        SystemMessagePromptTemplate.from_template(text),
        # ('human','text1')
        HumanMessagePromptTemplate.from_template("{text2}")

    ]
)
result = client.invoke(chat_template.format_prompt(language="英文",text2=text1))
print( result)


# result2 = client.invoke(chat_template.format_prompt(language="法语",text2=text1))
# print(result2)