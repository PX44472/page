#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
学习助手 Skill
功能：学习相关的理论，在AI时代能和Claude Code结合的理论，快速掌握某个主题
"""

import json
import requests
import re
from datetime import datetime

class LearningAssistantSkill:
    def __init__(self):
        """初始化学习助手Skill"""
        self.knowledge_base = {}
        self.learning_paths = {}
        self.code_examples = {}
        self.user_progress = {}
        self.claude_api_key = "eyJhbG...GJcAmg"  # 请替换为实际的Claude API密钥
        self.claude_api_url = "https://api.anthropic.com/v1/messages"
    
    def analyze_topic(self, topic):
        """
        分析学习主题，提取核心概念和关键知识点
        Args:
            topic: 学习主题
        Returns:
            dict: 包含核心概念、关键知识点和关联关系的分析结果
        """
        print(f"正在分析学习主题: {topic}")
        
        # 使用Claude API分析主题
        prompt = f"请分析以下学习主题，提取核心概念、关键知识点，并说明它们之间的关联关系：{topic}"
        response = self._call_claude(prompt)
        
        # 解析Claude的响应
        analysis = {
            "core_concepts": [],
            "key_knowledge_points": [],
            "relationships": []
        }
        
        # 简单的解析逻辑，实际应用中可能需要更复杂的NLP处理
        lines = response.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            if "核心概念" in line:
                current_section = "core_concepts"
            elif "关键知识点" in line:
                current_section = "key_knowledge_points"
            elif "关联关系" in line:
                current_section = "relationships"
            elif line and current_section:
                analysis[current_section].append(line)
        
        return analysis
    
    def generate_learning_path(self, topic, user_level="beginner"):
        """
        生成个性化学习路径
        Args:
            topic: 学习主题
            user_level: 用户知识水平 (beginner, intermediate, advanced)
        Returns:
            list: 学习路径，包含多个学习阶段
        """
        print(f"正在为主题 '{topic}' 生成学习路径，用户水平: {user_level}")
        
        # 分析主题
        topic_analysis = self.analyze_topic(topic)
        
        # 使用Claude API生成学习路径
        prompt = f"基于以下主题分析，为{user_level}水平的用户生成一个分阶段的学习路径：\n"
        prompt += f"核心概念: {', '.join(topic_analysis['core_concepts'])}\n"
        prompt += f"关键知识点: {', '.join(topic_analysis['key_knowledge_points'])}\n"
        prompt += "请按照从基础到高级的顺序，每个阶段包含明确的学习目标、学习内容和预计学习时间。"
        
        response = self._call_claude(prompt)
        
        # 解析学习路径
        learning_path = []
        stages = re.split(r'阶段\s*\d+', response)
        
        for i, stage in enumerate(stages[1:], 1):
            stage_info = {
                "stage": i,
                "content": stage.strip(),
                "estimated_time": ""
            }
            # 提取预计学习时间
            time_match = re.search(r'预计学习时间[:：]\s*(.*)', stage)
            if time_match:
                stage_info["estimated_time"] = time_match.group(1)
            
            learning_path.append(stage_info)
        
        # 保存学习路径
        self.learning_paths[topic] = learning_path
        
        return learning_path
    
    def get_theoretical_explanation(self, topic, concept):
        """
        获取理论知识解释
        Args:
            topic: 学习主题
            concept: 具体概念
        Returns:
            str: 概念的详细解释
        """
        print(f"正在获取 '{concept}' 的理论解释")
        
        # 使用Claude API获取理论解释
        prompt = f"请详细解释{topic}中的'{concept}'概念，包括其定义、原理、应用场景等。"
        response = self._call_claude(prompt)
        
        return response
    
    def get_code_example(self, topic, concept):
        """
        获取与概念相关的代码示例
        Args:
            topic: 学习主题
            concept: 具体概念
        Returns:
            str: 代码示例和解释
        """
        print(f"正在获取与 '{concept}' 相关的代码示例")
        
        # 使用Claude API生成代码示例
        prompt = f"请为{topic}中的'{concept}'概念提供一个详细的代码示例，包括代码解释和运行说明。"
        response = self._call_claude(prompt)
        
        # 保存代码示例
        if topic not in self.code_examples:
            self.code_examples[topic] = {}
        self.code_examples[topic][concept] = response
        
        return response
    
    def solve_coding_problem(self, problem_description):
        """
        解决编程问题
        Args:
            problem_description: 问题描述
        Returns:
            str: 解决方案和代码
        """
        print(f"正在解决编程问题: {problem_description}")
        
        # 使用Claude API解决问题
        prompt = f"请解决以下编程问题，并提供详细的代码和解释：{problem_description}"
        response = self._call_claude(prompt)
        
        return response
    
    def create_practice_project(self, topic, difficulty="medium"):
        """
        创建实践项目
        Args:
            topic: 学习主题
            difficulty: 项目难度 (easy, medium, hard)
        Returns:
            str: 项目描述和要求
        """
        print(f"正在为主题 '{topic}' 创建难度为 '{difficulty}' 的实践项目")
        
        # 使用Claude API创建实践项目
        prompt = f"请为{topic}主题创建一个{difficulty}难度的实践项目，包括项目描述、功能要求、技术栈建议和评估标准。"
        response = self._call_claude(prompt)
        
        return response
    
    def track_learning_progress(self, user_id, topic, progress):
        """
        跟踪学习进度
        Args:
            user_id: 用户ID
            topic: 学习主题
            progress: 学习进度 (0-100)
        """
        if user_id not in self.user_progress:
            self.user_progress[user_id] = {}
        
        self.user_progress[user_id][topic] = {
            "progress": progress,
            "last_updated": datetime.now().isoformat()
        }
        
        print(f"用户 {user_id} 在主题 '{topic}' 的学习进度已更新为 {progress}%")
    
    def get_learning_recommendation(self, user_id):
        """
        获取学习建议
        Args:
            user_id: 用户ID
        Returns:
            str: 个性化学习建议
        """
        if user_id not in self.user_progress:
            return "暂无学习记录，建议开始一个新的学习主题。"
        
        # 分析用户学习进度
        progress_data = self.user_progress[user_id]
        prompt = "基于以下学习进度数据，提供个性化的学习建议：\n"
        
        for topic, data in progress_data.items():
            prompt += f"- 主题: {topic}\n"
            prompt += f"  进度: {data['progress']}%\n"
            prompt += f"  最后更新: {data['last_updated']}\n"
        
        # 使用Claude API生成学习建议
        response = self._call_claude(prompt)
        
        return response
    
    def generate_questions(self, topic, difficulty="medium", question_type="multiple_choice", count=5):
        """
        生成题目
        Args:
            topic: 学习主题
            difficulty: 题目难度 (easy, medium, hard)
            question_type: 题目类型 (multiple_choice, true_false, short_answer)
            count: 题目数量
        Returns:
            list: 题目列表
        """
        print(f"正在为主题 '{topic}' 生成 {count} 道 {difficulty} 难度的 {question_type} 题目")
        
        # 使用Claude API生成题目
        prompt = f"请为{topic}主题生成{count}道{difficulty}难度的{question_type}题目，每道题目包括问题、选项（如果适用）和正确答案。"
        response = self._call_claude(prompt)
        
        # 解析题目
        questions = []
        # 简单的解析逻辑，实际应用中可能需要更复杂的NLP处理
        lines = response.split('\n')
        current_question = {}
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 处理问题行
            if line.startswith('问题') or line.startswith('题目'):
                if current_question:
                    questions.append(current_question)
                    current_question = {}
                # 提取问题内容
                if ':' in line:
                    current_question['question'] = line.split(':', 1)[1].strip()
                else:
                    current_question['question'] = line
            # 处理选项行
            elif line.startswith('选项') or line.startswith('A.') or line.startswith('B.') or line.startswith('C.') or line.startswith('D.'):
                if 'options' not in current_question:
                    current_question['options'] = []
                current_question['options'].append(line)
            # 处理答案行
            elif line.startswith('正确答案') or line.startswith('答案'):
                if ':' in line:
                    current_question['answer'] = line.split(':', 1)[1].strip()
                else:
                    current_question['answer'] = line
        
        # 处理最后一个问题
        if current_question:
            questions.append(current_question)
        
        # 如果没有解析到题目，手动创建一些示例题目
        if not questions:
            questions = [
                {
                    "question": "Pandas库中用于读取CSV文件的函数是什么？",
                    "options": ["A: read_csv()", "B: load_csv()", "C: import_csv()", "D: get_csv()"],
                    "answer": "A"
                },
                {
                    "question": "以下哪个不是Pandas的主要数据结构？",
                    "options": ["A: Series", "B: DataFrame", "C: Array", "D: Panel"],
                    "answer": "C"
                },
                {
                    "question": "要查看DataFrame的前5行数据，应该使用哪个方法？",
                    "options": ["A: head()", "B: top()", "C: first()", "D: preview()"],
                    "answer": "A"
                },
                {
                    "question": "处理DataFrame中缺失值的方法不包括以下哪项？",
                    "options": ["A: dropna()", "B: fillna()", "C: replace()", "D: remove()"],
                    "answer": "D"
                },
                {
                    "question": "Pandas中用于按列分组并计算聚合值的方法是？",
                    "options": ["A: groupby()", "B: aggregate()", "C: group()", "D: combine()"],
                    "answer": "A"
                }
            ]
        
        return questions
    
    def check_answer(self, question, user_answer):
        """
        检查答案
        Args:
            question: 题目
            user_answer: 用户答案
        Returns:
            dict: 检查结果，包含是否正确和解释
        """
        print(f"检查答案: 问题='{question.get('question', '')}', 用户答案='{user_answer}', 正确答案='{question.get('answer', '')}'")
        
        is_correct = user_answer.strip().lower() == question.get('answer', '').strip().lower()
        
        # 生成答案解释
        prompt = f"对于问题：'{question.get('question', '')}'，正确答案是'{question.get('answer', '')}'，请解释为什么这个答案是正确的。"
        explanation = self._call_claude(prompt)
        
        return {
            "is_correct": is_correct,
            "explanation": explanation,
            "correct_answer": question.get('answer', '')
        }
    
    def take_quiz(self, topic, difficulty="medium", question_type="multiple_choice", count=5):
        """
        进行测验
        Args:
            topic: 学习主题
            difficulty: 题目难度 (easy, medium, hard)
            question_type: 题目类型 (multiple_choice, true_false, short_answer)
            count: 题目数量
        Returns:
            dict: 测验结果，包含得分和每道题的情况
        """
        print(f"开始{topic}主题的测验，难度：{difficulty}，类型：{question_type}，题目数量：{count}")
        
        # 生成题目
        questions = self.generate_questions(topic, difficulty, question_type, count)
        
        # 存储测验结果
        quiz_result = {
            "topic": topic,
            "difficulty": difficulty,
            "question_type": question_type,
            "total_questions": count,
            "correct_answers": 0,
            "questions": []
        }
        
        # 模拟用户答题（实际应用中可以通过用户输入获取答案）
        for i, question in enumerate(questions):
            print(f"\n第{i+1}题: {question.get('question', '')}")
            if 'options' in question:
                for option in question['options']:
                    print(option)
            
            # 这里使用正确答案作为模拟用户答案，实际应用中应该让用户输入
            user_answer = question.get('answer', '')
            print(f"用户答案: {user_answer}")
            
            # 检查答案
            check_result = self.check_answer(question, user_answer)
            
            # 更新测验结果
            if check_result['is_correct']:
                quiz_result['correct_answers'] += 1
            
            quiz_result['questions'].append({
                "question": question.get('question', ''),
                "options": question.get('options', []),
                "user_answer": user_answer,
                "correct_answer": check_result['correct_answer'],
                "is_correct": check_result['is_correct'],
                "explanation": check_result['explanation']
            })
        
        # 计算得分
        quiz_result['score'] = (quiz_result['correct_answers'] / quiz_result['total_questions']) * 100
        
        print(f"\n测验完成！得分：{quiz_result['score']}%")
        print(f"正确答案数量：{quiz_result['correct_answers']}/{quiz_result['total_questions']}")
        
        return quiz_result
    
    def _call_claude(self, prompt):
        """
        调用Claude API
        Args:
            prompt: 提示词
        Returns:
            str: Claude的响应
        """
        # 模拟响应数据，以便在没有API密钥的情况下也能展示功能
        if "分析以下学习主题" in prompt:
            return "核心概念:\n- 数据清洗\n- 数据可视化\n- 统计分析\n- 机器学习\n\n关键知识点:\n- NumPy库\n- Pandas库\n- Matplotlib库\n- Seaborn库\n- 描述性统计\n- 假设检验\n\n关联关系:\n- 数据清洗是数据分析的基础\n- 数据可视化用于展示分析结果\n- 统计分析提供数据洞察\n- 机器学习用于预测和分类"
        elif "生成一个分阶段的学习路径" in prompt:
            return "阶段 1: Python基础\n学习目标: 掌握Python基本语法和数据结构\n学习内容: Python变量、数据类型、控制流、函数、列表、字典等\n预计学习时间: 1-2周\n\n阶段 2: NumPy和Pandas基础\n学习目标: 掌握数据处理库的基本使用\n学习内容: NumPy数组操作、Pandas Series和DataFrame、数据读取和写入\n预计学习时间: 1-2周\n\n阶段 3: 数据清洗和预处理\n学习目标: 掌握数据清洗和预处理技巧\n学习内容: 缺失值处理、异常值检测、数据转换、特征工程\n预计学习时间: 1周\n\n阶段 4: 数据可视化\n学习目标: 掌握数据可视化方法\n学习内容: Matplotlib基础、Seaborn高级可视化、交互式可视化\n预计学习时间: 1周\n\n阶段 5: 统计分析\n学习目标: 掌握基本统计分析方法\n学习内容: 描述性统计、假设检验、相关性分析\n预计学习时间: 1周\n\n阶段 6: 机器学习基础\n学习目标: 掌握机器学习基本概念和算法\n学习内容: 监督学习、无监督学习、模型评估\n预计学习时间: 2周"
        elif "详细解释" in prompt and "Pandas库" in prompt:
            return "Pandas是Python中用于数据处理和分析的强大库，它提供了两种主要的数据结构：Series（一维数组）和DataFrame（二维表格）。\n\nPandas的主要功能包括：\n1. 数据读取和写入：支持多种文件格式，如CSV、Excel、JSON等\n2. 数据清洗：处理缺失值、重复值、异常值\n3. 数据转换：数据类型转换、数据标准化\n4. 数据查询和筛选：使用条件表达式筛选数据\n5. 数据聚合和分组：使用groupby进行数据分组和聚合\n6. 时间序列分析：处理时间序列数据\n7. 数据合并和连接：合并多个数据集\n\nPandas的应用场景非常广泛，包括数据科学、金融分析、市场营销、社会科学研究等领域。它是Python数据分析生态系统的核心库之一，与NumPy、Matplotlib等库配合使用，可以完成从数据获取到分析、可视化的完整流程。"
        elif "提供一个详细的代码示例" in prompt and "Pandas库" in prompt:
            return "以下是一个使用Pandas库进行数据处理的代码示例：\n\n```python\nimport pandas as pd\nimport numpy as np\n\n# 1. 读取CSV文件\ndf = pd.read_csv('data.csv')\n\n# 2. 查看数据基本信息\nprint(df.head())  # 查看前5行数据\nprint(df.info())  # 查看数据类型和缺失值情况\nprint(df.describe())  # 查看数值型数据的统计信息\n\n# 3. 数据清洗\n# 处理缺失值\ndf = df.dropna()  # 删除包含缺失值的行\n# 或\ndf = df.fillna(0)  # 将缺失值填充为0\n\n# 4. 数据转换\n# 转换数据类型\ndf['age'] = df['age'].astype(int)\n\n# 5. 数据筛选\nadult_df = df[df['age'] >= 18]  # 筛选年龄大于等于18的行\n\n# 6. 数据聚合\nage_group = df.groupby('age')['income'].mean()  # 按年龄分组计算平均收入\n\n# 7. 数据可视化\nimport matplotlib.pyplot as plt\nage_group.plot(kind='bar')\nplt.title('Average Income by Age')\nplt.xlabel('Age')\nplt.ylabel('Average Income')\nplt.show()\n```\n\n这个示例展示了Pandas的基本操作，包括数据读取、查看、清洗、转换、筛选、聚合和可视化。实际应用中，根据具体需求，可能需要使用更多的Pandas功能。"
        elif "解决以下编程问题" in prompt:
            return """
要使用Pandas读取CSV文件并计算列的平均值，可以按照以下步骤操作：

```python
import pandas as pd

# 1. 读取CSV文件
df = pd.read_csv('data.csv')

# 2. 计算指定列的平均值
column_name = 'value'  # 替换为实际的列名
mean_value = df[column_name].mean()
print(f"{column_name}列的平均值: {mean_value}")

# 3. 计算所有数值列的平均值
mean_values = df.mean()
print("所有数值列的平均值:")
print(mean_values)
```

如果CSV文件包含非数值列，Pandas会自动跳过这些列，只计算数值列的平均值。

如果需要处理缺失值，可以在计算平均值之前使用`dropna()`或`fillna()`方法：

```python
# 方法1：删除包含缺失值的行
df_clean = df.dropna()
mean_value = df_clean[column_name].mean()

# 方法2：将缺失值填充为0
df_filled = df.fillna(0)
mean_value = df_filled[column_name].mean()
```
"""
        elif "创建一个" in prompt and "实践项目" in prompt:
            return "# Python数据分析实践项目：销售数据分析\n\n## 项目描述\n分析一家电商平台的销售数据，提取有价值的业务 insights，为业务决策提供支持。\n\n## 功能要求\n1. 数据读取和清洗：\n   - 读取销售数据CSV文件\n   - 处理缺失值和异常值\n   - 数据类型转换和标准化\n\n2. 数据探索和分析：\n   - 销售趋势分析（按时间）\n   - 产品类别销售分析\n   - 客户购买行为分析\n   - 地区销售分布分析\n\n3. 数据可视化：\n   - 销售趋势折线图\n   - 产品类别销售饼图\n   - 客户购买行为柱状图\n   - 地区销售热力图\n\n4. 结果报告：\n   - 生成HTML格式的分析报告\n   - 包含关键发现和建议\n\n## 技术栈建议\n- Python 3.7+\n- Pandas：数据处理\n- Matplotlib/Seaborn：数据可视化\n- Jupyter Notebook：交互式分析\n- NumPy：数值计算\n\n## 评估标准\n1. 代码质量：结构清晰，注释完整\n2. 分析深度：能够提取有价值的业务 insights\n3. 可视化效果：图表美观，信息传递清晰\n4. 报告质量：内容完整，逻辑清晰\n\n## 数据说明\n可以使用以下开源数据集：\n- [Kaggle: E-Commerce Sales Data](https://www.kaggle.com/datasets/carrie1/ecommerce-data)\n- 或使用模拟数据进行练习\n\n## 预期成果\n完成本项目后，你将能够：\n- 熟练使用Pandas进行数据处理和分析\n- 掌握数据可视化技巧\n- 具备从数据中提取业务 insights的能力\n- 能够生成专业的数据分析报告"
        elif "基于以下学习进度数据" in prompt:
            return "基于您的学习进度数据，以下是个性化的学习建议：\n\n1. 您在'Python数据分析'主题的学习进度为60%，已经完成了大部分基础内容。\n\n2. 建议接下来的学习重点：\n   - 深入学习Pandas的高级功能，如数据透视表、多索引等\n   - 学习使用scikit-learn库进行机器学习\n   - 实践一个完整的数据分析项目，将所学知识应用到实际场景\n\n3. 学习资源推荐：\n   - 《Python for Data Analysis》（Wes McKinney著）\n   - Kaggle平台的数据分析竞赛\n   - DataCamp的Python数据分析课程\n\n4. 学习时间安排：\n   - 高级Pandas功能：1周\n   - 机器学习基础：2周\n   - 实践项目：2-3周\n\n5. 学习方法建议：\n   - 结合理论学习和实际练习\n   - 参与数据分析社区，与其他学习者交流\n   - 定期回顾和总结所学知识\n\n希望这些建议对您的学习有所帮助！"
        elif "生成题目" in prompt or "生成测验" in prompt:
            return "问题1: Pandas库中用于读取CSV文件的函数是什么？\n选项A: read_csv()\n选项B: load_csv()\n选项C: import_csv()\n选项D: get_csv()\n正确答案: A\n\n问题2: 以下哪个不是Pandas的主要数据结构？\n选项A: Series\n选项B: DataFrame\n选项C: Array\n选项D: Panel\n正确答案: C\n\n问题3: 要查看DataFrame的前5行数据，应该使用哪个方法？\n选项A: head()\n选项B: top()\n选项C: first()\n选项D: preview()\n正确答案: A\n\n问题4: 处理DataFrame中缺失值的方法不包括以下哪项？\n选项A: dropna()\n选项B: fillna()\n选项C: replace()\n选项D: remove()\n正确答案: D\n\n问题5: Pandas中用于按列分组并计算聚合值的方法是？\n选项A: groupby()\n选项B: aggregate()\n选项C: group()\n选项D: combine()\n正确答案: A"
        elif "解释为什么这个答案是正确的" in prompt:
            if "Pandas库中用于读取CSV文件的函数" in prompt:
                return "在Pandas库中，read_csv()是专门用于读取CSV文件的函数。它可以将CSV文件读取为DataFrame对象，支持多种参数来控制读取行为，如分隔符、编码、列名等。而其他选项如load_csv()、import_csv()和get_csv()都不是Pandas库中用于读取CSV文件的标准函数。"
            elif "不是Pandas的主要数据结构" in prompt:
                return "Pandas的主要数据结构包括：1. Series（一维数组）、2. DataFrame（二维表格）、3. Panel（三维数据结构，在较新版本中已被弃用）。而Array是NumPy库的主要数据结构，不是Pandas特有的。"
            elif "查看DataFrame的前5行数据" in prompt:
                return "head()是Pandas DataFrame的方法，默认返回前5行数据。可以通过参数指定返回的行数，如head(10)返回前10行。其他选项如top()、first()和preview()都不是Pandas中用于查看前几行数据的标准方法。"
            elif "处理DataFrame中缺失值的方法" in prompt:
                return "Pandas中处理缺失值的方法包括：1. dropna() - 删除包含缺失值的行或列；2. fillna() - 填充缺失值；3. replace() - 替换缺失值。而remove()不是Pandas中专门用于处理缺失值的方法。"
            elif "按列分组并计算聚合值的方法" in prompt:
                return "groupby()是Pandas中用于按一个或多个列对数据进行分组的方法，分组后可以使用聚合函数（如sum、mean、count等）计算每组的统计值。aggregate()是用于聚合计算的方法，但它通常与groupby()一起使用。group()和combine()不是Pandas中用于分组的标准方法。"
        
        # 实际API调用代码（注释掉，以便使用模拟数据）
        """
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self.claude_api_key,
            "anthropic-version": "2023-06-01"
        }
        
        data = {
            "model": "claude-3-opus-20240229",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 1000
        }
        
        try:
            response = requests.post(self.claude_api_url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            return result['content'][0]['text']
        except Exception as e:
            print(f"调用Claude API时出错: {e}")
            return "抱歉，暂时无法获取响应，请稍后再试。"
        """
        return "这是一个模拟响应，实际应用中会调用Claude API获取真实内容。"
    
    def save_data(self, filename="learning_assistant_data.json"):
        """
        保存数据到文件
        Args:
            filename: 文件名
        """
        data = {
            "knowledge_base": self.knowledge_base,
            "learning_paths": self.learning_paths,
            "code_examples": self.code_examples,
            "user_progress": self.user_progress
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"数据已保存到 {filename}")
    
    def load_data(self, filename="learning_assistant_data.json"):
        """
        从文件加载数据
        Args:
            filename: 文件名
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.knowledge_base = data.get("knowledge_base", {})
            self.learning_paths = data.get("learning_paths", {})
            self.code_examples = data.get("code_examples", {})
            self.user_progress = data.get("user_progress", {})
            
            print(f"数据已从 {filename} 加载")
        except Exception as e:
            print(f"加载数据时出错: {e}")

def main():
    """主函数"""
    # 创建学习助手实例
    assistant = LearningAssistantSkill()
    
    # 示例用法
    print("=== 学习助手Skill 示例 ===")
    
    # 1. 分析主题
    topic = "Python数据分析"
    print(f"\n1. 分析主题: {topic}")
    analysis = assistant.analyze_topic(topic)
    print("核心概念:", analysis["core_concepts"])
    print("关键知识点:", analysis["key_knowledge_points"])
    
    # 2. 生成学习路径
    print(f"\n2. 为主题 '{topic}' 生成学习路径")
    learning_path = assistant.generate_learning_path(topic, "beginner")
    for stage in learning_path:
        print(f"\n阶段 {stage['stage']}:")
        print(stage['content'])
    
    # 3. 获取理论解释
    concept = "Pandas库"
    print(f"\n3. 获取 '{concept}' 的理论解释")
    explanation = assistant.get_theoretical_explanation(topic, concept)
    print(explanation)
    
    # 4. 获取代码示例
    print(f"\n4. 获取与 '{concept}' 相关的代码示例")
    code_example = assistant.get_code_example(topic, concept)
    print(code_example)
    
    # 5. 解决编程问题
    problem = "如何使用Pandas读取CSV文件并计算列的平均值"
    print(f"\n5. 解决编程问题: {problem}")
    solution = assistant.solve_coding_problem(problem)
    print(solution)
    
    # 6. 创建实践项目
    print(f"\n6. 为主题 '{topic}' 创建实践项目")
    project = assistant.create_practice_project(topic, "medium")
    print(project)
    
    # 7. 跟踪学习进度
    user_id = "user123"
    print(f"\n7. 跟踪用户 {user_id} 的学习进度")
    assistant.track_learning_progress(user_id, topic, 60)
    
    # 8. 获取学习建议
    print(f"\n8. 获取用户 {user_id} 的学习建议")
    recommendation = assistant.get_learning_recommendation(user_id)
    print(recommendation)
    
    # 9. 保存数据
    print("\n9. 保存数据")
    assistant.save_data()

if __name__ == "__main__":
    main()
