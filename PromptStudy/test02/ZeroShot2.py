#零样本提示（Zero-Shot）
# pip install openai
#提示词在大模型应用中直接使用，也可以看到效果
from openai import OpenAI
import os
# 读取环境变量，创建客户端连接
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
client = OpenAI(api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",)

# 提示词
prompt = """
将文本分类为中性、负面或正面。
文本：我认为这家餐馆的菜品一般。
情感：
"""
# 在上面的提示中，我们没有向模型提供任何示例。
# 定义函数 get_completion
def get_completion(prompt, model="qwen-max-latest"):
    messages = [{"role": "user", "content": prompt}]
    # 获取模型返回结果
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  # 模型输出的随机性，0 表示随机性最小
    )
    #  返回模型回答内容
    return response.choices[0].message.content
# 打印结果
print(get_completion(prompt))

