#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
学习助手Skill使用示例
"""

from learning_assistant_skill import LearningAssistantSkill

# 初始化学习助手
assistant = LearningAssistantSkill()

print("=== 学习助手Skill使用示例 ===\n")

# 1. 分析学习主题
topic = "Python数据分析"
print("1. 分析学习主题:")
print(f"主题: {topic}")
analysis = assistant.analyze_topic(topic)
print("核心概念:", analysis["core_concepts"])
print("关键知识点:", analysis["key_knowledge_points"])
print()

# 2. 生成学习路径
print("2. 生成学习路径:")
learning_path = assistant.generate_learning_path(topic, "beginner")
for stage in learning_path:
    print(f"阶段 {stage['stage']}:")
    print(stage['content'])
    print()

# 3. 获取理论解释
concept = "Pandas库"
print(f"3. 获取 '{concept}' 的理论解释:")
explanation = assistant.get_theoretical_explanation(topic, concept)
print(explanation)
print()

# 4. 获取代码示例
print(f"4. 获取与 '{concept}' 相关的代码示例:")
code_example = assistant.get_code_example(topic, concept)
print(code_example)
print()

# 5. 解决编程问题
problem = "如何使用Pandas读取CSV文件并计算列的平均值"
print(f"5. 解决编程问题: {problem}")
solution = assistant.solve_coding_problem(problem)
print(solution)
print()

# 6. 创建实践项目
print(f"6. 为主题 '{topic}' 创建实践项目:")
project = assistant.create_practice_project(topic, "medium")
print(project)
print()

# 7. 跟踪学习进度
user_id = "user123"
print(f"7. 跟踪用户 {user_id} 的学习进度:")
assistant.track_learning_progress(user_id, topic, 60)
print()

# 8. 获取学习建议
print(f"8. 获取用户 {user_id} 的学习建议:")
recommendation = assistant.get_learning_recommendation(user_id)
print(recommendation)
print()

# 9. 保存数据
print("9. 保存数据:")
assistant.save_data()
print()

# 10. 生成题目
print("10. 生成题目:")
questions = assistant.generate_questions(topic, "medium", "multiple_choice", 5)
for i, q in enumerate(questions):
    print(f"\n第{i+1}题: {q.get('question', '')}")
    if 'options' in q:
        for option in q['options']:
            print(option)
    print(f"正确答案: {q.get('answer', '')}")
print()

# 11. 进行测验
print("11. 进行测验:")
quiz_result = assistant.take_quiz(topic, "medium", "multiple_choice", 5)
print()

print("=== 示例完成 ===")
