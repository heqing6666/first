# Learn B

## 在 VS Code 中使用 Git

1. 在 VS Code 中打开本项目，点击左侧「源代码管理」图标。
2. 在「更改」列表中点击文件旁的 `+`，将文件暂存（相当于 `git add`）。
3. 输入提交说明并点击「提交」（相当于 `git commit`）。
4. 点击「同步更改」或「推送」，将提交发送到 GitHub。
5. 在源代码管理面板确认没有待提交更改，并在 GitHub 仓库的提交记录中确认推送结果。
66666

## Conventional Commits 提交规范

提交信息使用 `类型: 简短说明` 的格式，类型后加冒号和空格。常见类型：

- `feat:` 新功能
- `fix:` 修复问题
- `docs:` 文档修改
- `refactor:` 重构代码，不改变功能
- `test:` 添加或修改测试
- `chore:` 日常维护或配置变更

示例：

```text
feat: add calculator history
fix: handle division by zero
docs: explain Git workflow
refactor: simplify input validation
```

说明应简洁、明确地描述本次提交内容。可以在 VS Code 源代码管理面板的提交说明框中输入规范格式，再点击「提交」。
