---
name: "github-push"
description: "推送到GitHub。当用户需要将代码推送到GitHub仓库时调用。"
---

# GitHub推送工具

## 功能
- 将本地Git仓库推送到GitHub
- 支持指定远程仓库URL
- 自动设置默认远程仓库

## 使用方法
1. 确保本地仓库已经初始化并提交了代码
2. 调用此skill时，需要提供GitHub仓库URL
3. 执行推送操作

## 示例
```bash
# 推送代码到GitHub
git remote add origin <GitHub仓库URL>
git push -u origin master
```

## 注意事项
- 需要先在GitHub上创建仓库
- 确保本地Git配置了正确的用户名和邮箱
- 可能需要输入GitHub账号密码或SSH密钥验证