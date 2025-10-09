# 应用实战3：企业运营成本分析核算
# 安装依赖库
# pip install openai
# pip install gradio
# 浏览器中访问：http://127.0.0.1:7860，需要填入的数据可从三一重工.json和中联重科.json中获得
import gradio as gr
from openai import OpenAI
import os
import datetime
# 从环境变量中获取DASHSCOPE_API_KEY
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
# 创建OpenAI客户端实例
client = OpenAI(api_key=DASHSCOPE_API_KEY,
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", )
import asyncio
class CostAnalysisPipeline:
    # 使用大模型进行问答
    def LLM_QA(self, llm_q):
        # 构建问答模板
        qa_template = f"""你是一个企业业绩分析专家，请回答以下问题：
        {llm_q}
        请给出详细和精确的分析。"""
        try:
            # 打印开始询问大模型的时间
            print(qa_template, "<==开始询问大模型，时间：", datetime.datetime.now())
            # 调用OpenAI API获取回答
            response = client.chat.completions.create(
                model="qwen-max-latest",
                messages=[{"role": "user", "content": qa_template}],
                stream=False
            )
            # 提取回答内容
            answer = response.choices[0].message.content.strip() if response.choices else "无法提供答案"
            print(f"完整回答: {answer}")
            return answer
        except Exception as e:
            # 捕获并打印API调用异常
            print(f"API调用失败: {e}")
            return "无法提供答案"

    # 从财务报表中提取关键指标
    def extract_financial_data(self, report_text):
        # 构建提取关键指标的提示
        prompt = (
            f"请从以下财务报表中提取关键指标：营业收入、净利润、每股收益、可以适当精简,但分析后需要保留发表日期时间信息"
            f"""总资产收益率、毛利率、净利率。\n\n,如果有多年数据，需要分析趋势
                输入数据：{report_text}"""
        )
        # 调用LLM_QA方法获取回答
        return self.LLM_QA(prompt)

    # 分析财务指标
    def analyze_financial_indicators(self, report_text):
        # 构建分析财务指标的提示
        prompt = (
            f"根据以下财务数据，计算营业收入同比增长率和净利润同比增长率，可以适当精简，但分析后需要保留发表日期时间信息"
            f"并生成年度对比分析。如果有多年数据，需要分析趋势\n\n输入数据：{report_text}"
        )
        # 调用LLM_QA方法获取回答
        return self.LLM_QA(prompt)

    # 预测未来趋势
    def predict_future_trends(self, report_text):
        # 构建预测未来趋势的提示
        prompt = (
            f"根据以下当前财务数据，预测未来三年的营业收入和净利润趋势。但分析后需要保留发表日期时间信息\n\n"
            f"输入数据：{report_text}"
        )
        # 调用LLM_QA方法获取回答
        return self.LLM_QA(prompt)

    # 优化成本
    def optimize_costs(self, report_text):
        # 构建优化成本的提示
        prompt = (
            f"根据以下业绩信息，提出业绩优化建议，可以适当精简,但分析后需要保留发表日期时间信息"
            f"如何提高企业的业绩效益。\n\n输入数据：{report_text}"
        )
        # 调用LLM_QA方法获取回答
        return self.LLM_QA(prompt)

    # 生成最终报告
    def generate_final_report(self, extracted_data, analysis_result, prediction_result, optimization_result):
        # 构建生成最终报告的提示
        prompt = (
            f"根据以下数据，生成一份企业业绩分析报告，"
            f"报告包含财务分析、趋势预测和业绩优化建议。可以适当精简,但分析后需要保留发表日期时间信息\n\n"
            f"提取的财务数据：{extracted_data}\n\n"
            f"财务分析：{analysis_result}\n\n"
            f"趋势预测：{prediction_result}\n\n"
            f"业绩优化建议：{optimization_result}"
        )
        # 调用LLM_QA方法获取回答
        return self.LLM_QA(prompt)

    # 比较两个报告
    def compare_reports(self, report1, report2):
        # 构建比较报告的提示
        prompt = (
            f"以下是两家公司或者同一个公司不同时期财务分析报告，请先判断这是一个公司的不同时间报告还是不同公司的报告，然后对它们进行比较,需要关注财报的发表日期。可以适当精简\n\n"
            f"数据1的报告：{report1}\n\n"
            f"数据2的报告：{report2}"
        )
        # 调用LLM_QA方法获取回答
        return self.LLM_QA(prompt)


# 异步分析数据
async def analyze_data(report_text):
    # 创建CostAnalysisPipeline实例
    pipeline = CostAnalysisPipeline()
    results = []

    # 提取财务数据
    extracted_data = pipeline.extract_financial_data(report_text)
    results.append(f"提取的财务数据:\n{extracted_data}\n")

    # 分析财务指标
    analysis_result = pipeline.analyze_financial_indicators(report_text)
    results.append(f"财务指标分析:\n{analysis_result}\n")

    # 预测未来趋势
    prediction_result = pipeline.predict_future_trends(report_text)
    results.append(f"未来趋势预测:\n{prediction_result}\n")

    # 优化业绩
    optimization_result = pipeline.optimize_costs(report_text)
    results.append(f"业绩优化建议:\n{optimization_result}\n")

    # 生成最终报告
    final_report = pipeline.generate_final_report(
        extracted_data, analysis_result, prediction_result, optimization_result
    )
    results.append(f"企业业绩分析报告:\n{final_report}\n")

    # 返回所有结果的组合（包括每一次的返回结果）
    return "\n".join(results), final_report


# 异步比较两个报告
async def compare_reports(report1, report2):
    # 创建CostAnalysisPipeline实例
    pipeline = CostAnalysisPipeline()
    # 调用compare_reports方法获取比较结果
    return pipeline.compare_reports(report1, report2)


# 创建Gradio界面
with gr.Blocks() as demo:
    gr.Markdown("## 企业业绩分析")
    with gr.Row():
        with gr.Column():
            # 输入框1，用于输入财务报表文本
            input1 = gr.Textbox(label="输入数据 1 (财务报表文本)", placeholder="请输入财务报表内容...")
            # 分析按钮1
            analyze_button1 = gr.Button("分析 1")
            # 输出框1，用于显示分析结果
            output1 = gr.Markdown(label="分析结果 1")

        with gr.Column():
            # 输入框2，用于输入财务报表文本
            input2 = gr.Textbox(label="输入数据 2 (财务报表文本)", placeholder="请输入财务报表内容...")
            # 分析按钮2
            analyze_button2 = gr.Button("分析 2")
            # 输出框2，用于显示分析结果
            output2 = gr.Markdown(label="分析结果 2")

    # 绑定分析按钮1和输入框1到analyze_data函数
    analyze_button1.click(analyze_data, inputs=input1, outputs=[output1, output1])
    # 绑定分析按钮2和输入框2到analyze_data函数
    analyze_button2.click(analyze_data, inputs=input2, outputs=[output2, output2])

    # 比较按钮
    compare_button = gr.Button("比较报告")
    # 输出框，用于显示比较结果
    compare_output = gr.Markdown(label="比较结果")

    # 绑定比较按钮到compare_reports函数
    compare_button.click(compare_reports, inputs=[output1, output2], outputs=compare_output)

# 启动Gradio界面
if __name__ == "__main__":
    demo.launch()
