from openai import OpenAI
from dotenv import load_dotenv
import numpy as np
from numpy import dot
from numpy.linalg import norm
import os

from openai import OpenAI

API_BASE_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=API_BASE_URL,
)


def cos_sim(a, b):
    '''余弦距离 -- 越大越相似'''
    return dot(a, b) / (norm(a) * norm(b))


def l2(a, b):
    '''欧式距离 -- 越小越相似'''
    x = np.asarray(a) - np.asarray(b)
    return norm(x)


def get_embeddings(texts, model="text-embedding-v3"):
    data = client.embeddings.create(input=texts, model=model).data
    # print(data)
    # 返回了一个包含所有嵌入表示的列表
    return [x.embedding for x in data]


# 且能支持跨语言
# query = "global conflicts"
query = "国际争端"
documents = [
    "联合国安理会上，俄罗斯与美国，伊朗与以色列“吵”起来了",
    "土耳其、芬兰、瑞典与北约代表将继续就瑞典“入约”问题进行谈判",
    "日本岐阜市陆上自卫队射击场内发生枪击事件 3人受伤",
    "孙志刚被判死缓 减为无期徒刑后终身监禁 不得减刑、假释",
    "以色列立法禁联合国机构，美表态担忧，中东局势再生波澜",
]
#向量化：获取查询的嵌入表示和文档的嵌入表示
query_vec = get_embeddings([query])[0]
doc_vecs = get_embeddings(documents)

print("Cosine distance:")
print(cos_sim(query_vec, query_vec))
for vec in doc_vecs:
    print(cos_sim(query_vec, vec))

print("\nEuclidean distance:")
print(l2(query_vec, query_vec))
for vec in doc_vecs:
    print(l2(query_vec, vec))