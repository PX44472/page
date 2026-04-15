#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
学习助手Skill - 理论知识学习示例
"""

from learning_assistant_skill import LearningAssistantSkill

# 初始化学习助手
assistant = LearningAssistantSkill()

print("=== 学习助手Skill - 理论知识学习示例 ===\n")

# 选择学习主题
topic = "Python数据分析"
print(f"学习主题: {topic}\n")

# 1. 分析主题，了解核心概念和关键知识点
print("1. 分析主题，了解核心概念和关键知识点:")
analysis = assistant.analyze_topic(topic)
print("核心概念:")
for concept in analysis["core_concepts"]:
    print(f"  - {concept}")
print("关键知识点:")
for point in analysis["key_knowledge_points"]:
    print(f"  - {point}")
print()

# 2. 生成学习路径，了解学习顺序
print("2. 生成学习路径，了解学习顺序:")
learning_path = assistant.generate_learning_path(topic, "beginner")
for stage in learning_path:
    print(f"阶段 {stage['stage']}:")
    print(stage['content'])
    print()

# 3. 学习具体概念的理论知识
print("3. 学习具体概念的理论知识:")

# 选择要学习的概念
concepts_to_learn = ["Pandas库", "NumPy库", "数据清洗", "数据可视化"]

for concept in concepts_to_learn:
    print(f"\n学习概念: {concept}")
    explanation = assistant.get_theoretical_explanation(topic, concept)
    print(explanation)
    print("-" * 80)

# 4. 获取与概念相关的代码示例，加深理解
print("4. 获取与概念相关的代码示例，加深理解:")

for concept in concepts_to_learn[:2]:  # 只展示前两个概念的代码示例
    print(f"\n概念: {concept} 的代码示例:")
    code_example = assistant.get_code_example(topic, concept)
    print(code_example)
    print("-" * 80)

# 5. 通过做题巩固所学知识
print("5. 通过做题巩固所学知识:")
quiz_result = assistant.take_quiz(topic, "medium", "multiple_choice", 5)
print(f"测验得分: {quiz_result['score']}%")
print(f"正确答案数量: {quiz_result['correct_answers']}/{quiz_result['total_questions']}")

# 6. 获取学习建议，规划后续学习
print("\n6. 获取学习建议，规划后续学习:")
user_id = "user123"
assistant.track_learning_progress(user_id, topic, 70)
recommendation = assistant.get_learning_recommendation(user_id)
print(recommendation)

print("\n=== 理论知识学习示例完成 ===")
print("\n通过以上步骤，你可以:")
print("1. 了解学习主题的核心概念和关键知识点")
print("2. 按照合理的学习路径进行学习")
print("3. 深入学习每个概念的理论知识")
print("4. 通过代码示例加深理解")
print("5. 通过做题巩固所学知识")
print("6. 根据学习建议规划后续学习")
