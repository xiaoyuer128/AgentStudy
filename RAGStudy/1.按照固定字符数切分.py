text = ("自然语言处理（NLP），作为计算机科学、人工智能与语言学的交融之地，致力于赋予计算机解析和处理人类语言的能力。"
        "在这个领域，机器学习发挥着至关重要的作用。利用多样的算法，机器得以分析、领会乃至创造我们所理解的语言。"
        "从机器翻译到情感分析，从自动摘要到实体识别，NLP的应用已遍布各个领域。随着深度学习技术的飞速进步，"
        "NLP的精确度与效能均实现了巨大飞跃。如今，部分尖端的NLP系统甚至能够处理复杂的语言理解任务，"
        "如问答系统、语音识别和对话系统等。NLP的研究推进不仅优化了人机交流，也对提升机器的自主性和智能水平起到了关键作用。")


def split_by_fixed_char_count(text, count):

    chunk =  [text[i:i + count] for i in range(0, len(text), count)]
    return  chunk
    # return [text[i:i + count] for i in range(0, len(text), count)]

    '''
    text[i:i + count] 是 Python 中的切片操作，用于从字符串 text 中提取子字符串。
    i:i
    i：切片的起始索引（包含）。
    i + count：切片的结束索引（不包含），如果 i + count 超出了字符串的长度，则提取到字符串的末尾为止

    range() 是 Python 中的一个内置函数，用于生成一个整数序列；
    num=[1,2,3,4,5,6]    --列表的长度--len(num) --6    range(0,len(num),2)--[0,1,2,3,4,5]---[0,2,4]
    range(start, stop, step)： start：序列的起始值（包含），默认为 0。
    stop：序列的结束值（不包含）。 step：序列中每个数字之间的步长，默认为 1。
    比如：range(1, 5, 2) 生成序列：1, 3     1,2,3,4  步长为2

    将输入的字符串 text 按照指定的字符数 count 进行分割，返回一个列表，其中每个元素是长度为 count 的子字符串。
    如果最后一个子字符串不足 count 长度，则保持原样。
    使用列表推导式遍历字符串。每次从索引 i 开始截取长度为 count 的子字符串。
    索引步长为 count，确保每次跳过已处理的部分。
    '''

chunks = split_by_fixed_char_count(text, 50)
for i, chunk in enumerate(chunks):
    print(f"块 {i} - 长度{len(chunk)}，内容: {chunk}")



'''
enumerate() 是 Python 中的一个内置函数，
用于将一个可迭代对象（如列表）组合为一个索引序列，
同时列出数据和数据的下标。
enumerate(chunks) 的作用是为 chunks 列表中的每个子字符串生成一个索引，并将其与子字符串配对。
这样在循环中可以同时访问子字符串的索引和内容。
'''
# # 基本用法
# fruits = ['apple', 'banana', 'orange']
# for index, fruit in enumerate(fruits):
#     print(f"索引 {index}: {fruit}")
#
# # 输出:
# # 索引 0: apple
# # 索引 1: banana
# # 索引 2: orange
#
# # 指定起始索引
# for index, fruit in enumerate(fruits, start=1):
#     print(f"第 {index} 个: {fruit}")
#
# # 输出:
# # 第 1 个: apple
# # 第 2 个: banana
# # 第 3 个: orange
