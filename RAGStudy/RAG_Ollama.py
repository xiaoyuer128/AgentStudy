import ollama  # pip install ollama
#核心代码
def get_embedding(text, model="bge-m3"):
    response =  ollama.embed(model,text)
    print(response)
    embedding =  response['embeddings']
    return embedding
test_query =  '我爱你'
vec = get_embedding(test_query)
print(vec[0])
print('维度：',len(vec[0]))