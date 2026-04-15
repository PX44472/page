# 学习助手 Skill 使用指南

## 功能介绍

学习助手Skill是一个结合理论学习和代码实践的智能学习工具，主要功能包括：

1. **理论学习与解释**：提供系统化的理论知识讲解，支持多领域的知识覆盖
2. **AI辅助学习策略**：基于AI的个性化学习路径推荐，智能学习进度跟踪
3. **快速主题掌握**：主题概览和核心概念提取，重点内容快速学习
4. **Claude Code集成**：代码示例与实践，问题解决与调试，项目实践

## 安装与配置

### 安装依赖

```bash
pip install requests
```

### 配置Claude API

1. 在`learning_assistant_skill.py`文件中，找到以下代码行：

```python
self.claude_api_key = "YOUR_CLAUDE_API_KEY"  # 请替换为实际的Claude API密钥
```

2. 将`YOUR_CLAUDE_API_KEY`替换为您的实际Claude API密钥。

## 使用方法

### 基本使用流程

1. **初始化学习助手**

```python
from learning_assistant_skill import LearningAssistantSkill

assistant = LearningAssistantSkill()
```

2. **分析学习主题**

```python
topic = "Python数据分析"
analysis = assistant.analyze_topic(topic)
print("核心概念:", analysis["core_concepts"])
print("关键知识点:", analysis["key_knowledge_points"])
```

3. **生成学习路径**

```python
learning_path = assistant.generate_learning_path(topic, "beginner")
for stage in learning_path:
    print(f"阶段 {stage['stage']}:")
    print(stage['content'])
```

4. **获取理论解释**

```python
concept = "Pandas库"
explanation = assistant.get_theoretical_explanation(topic, concept)
print(explanation)
```

5. **获取代码示例**

```python
code_example = assistant.get_code_example(topic, concept)
print(code_example)
```

6. **解决编程问题**

```python
problem = "如何使用Pandas读取CSV文件并计算列的平均值"
solution = assistant.solve_coding_problem(problem)
print(solution)
```

7. **创建实践项目**

```python
project = assistant.create_practice_project(topic, "medium")
print(project)
```

8. **跟踪学习进度**

```python
user_id = "user123"
assistant.track_learning_progress(user_id, topic, 60)
```

9. **获取学习建议**

```python
recommendation = assistant.get_learning_recommendation(user_id)
print(recommendation)
```

10. **保存和加载数据**

```python
# 保存数据
assistant.save_data()

# 加载数据
assistant.load_data()
```

### 示例运行

直接运行`learning_assistant_skill.py`文件，将执行一个完整的示例：

```bash
python learning_assistant_skill.py
```

## 技术实现

- **核心模块**：知识管理、学习策略、主题掌握、Claude Code集成
- **数据结构**：知识点图谱、学习路径、代码示例库、用户进度
- **API集成**：Claude API用于生成内容和解决问题
- **数据持久化**：JSON文件存储学习数据

## 扩展功能

1. **学习社区**：与其他学习者交流，分享学习经验和资源
2. **学习资源管理**：整合外部学习资源，推荐优质学习材料
3. **职业技能发展**：针对特定职业的技能培训，行业知识和趋势分析

## 注意事项

1. 使用前请确保已配置有效的Claude API密钥
2. 网络连接需要稳定，以便与Claude API进行通信
3. 首次运行时，生成内容可能需要一些时间，请耐心等待
4. 建议定期保存学习数据，以防数据丢失

## 故障排除

- **API调用失败**：检查API密钥是否正确，网络连接是否正常
- **学习路径生成失败**：尝试简化学习主题，确保主题明确具体
- **代码示例生成失败**：确保主题与编程相关，提供更具体的概念

## 联系方式

如有问题或建议，请联系开发者。
