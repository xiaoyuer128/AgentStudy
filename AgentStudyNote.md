## Prompt

提示词工程：<img src="C:\Users\XIaoYuer\AppData\Roaming\Typora\typora-user-images\image-20251008161508623.png" alt="image-20251008161508623" style="zoom: 67%;" />四要点

![image-20251008192451705](D:\Codeprctice\AgentStudy\image-20251008192451705.png)

插件：google 提示词优化器

![image-20251008193442104](C:\Users\XIaoYuer\AppData\Roaming\Typora\typora-user-images\image-20251008193442104.png)

简单问题：零样本提示、少样本提示

稍复杂问题：链式思考：给出思维过程（目前已经是大模型内置功能）

复杂问题：自我一致性、思维树

###### https://arxiv.org/pdf/2201.11903（Chain-of-Thought Prompting Elicits Reasoning in Large Language Models）



## 提示词攻击和防范

输入提示诱导大语言模型生成攻击者预期的输出，操控模型行为或泄露敏感信息

提示词注入

提示词越狱

提示词泄露

防范：1.在系统提示层面对输入内容进行检测

 			2.给模型固定身份固定范围，学会识别不合理请求



## 模型训练

反复调整超参数，初始参数随机，使用上一代参数来训练新一代的参数

自监督学习：人工介入较少

数据处理

#### 监督微调

举一反三

Meta 开源了 LLaMA
LLaMA1 ：[[2302.13971\] LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971)
LLaMA2 ： https://arxiv.org/abs/2307.09288
LLaMA3 ：https://huggingface.co/collections/meta-llama/meta-llama-3-66214712577ca38149ebb2b6
