# Kivy Android CI 构建测试

这是一个用于测试 Kivy 应用 Android 自动化构建的项目。

## 项目结构

```
kivy-android-ci/
├── .github/
│   └── workflows/
│       └── android.yml          # GitHub Actions 工作流配置
├── main.py                      # Kivy 应用主文件
├── buildozer.spec              # Buildozer 构建配置
└── README.md                   # 项目说明文档
```

## 功能特性

- 简单的 Kivy 应用示例
- 完整的 Android 构建配置
- GitHub Actions 自动化构建
- 构建缓存优化
- 构建失败时的日志上传

## 本地开发

### 环境要求

- Python 3.8+
- Kivy
- Buildozer (用于 Android 构建)

### 安装依赖

```bash
pip install kivy buildozer
```

### 运行应用

```bash
python main.py
```

### 本地 Android 构建

```bash
buildozer android debug
```

## CI/CD 构建

项目配置了 GitHub Actions 自动化构建，会在以下情况触发：

- 推送到 `main` 分支
- 创建针对 `main` 分支的 Pull Request
- 手动触发构建

### 构建产物

- 成功构建：APK 文件会作为 artifact 上传，保留 30 天
- 构建失败：构建日志会作为 artifact 上传，保留 7 天

### 构建优化

- 使用缓存加速构建过程
- 设置 60 分钟超时避免构建卡死
- 分别处理成功和失败的情况

## 配置说明

### buildozer.spec 主要配置

- **Target API**: 33 (Android 13)
- **Minimum API**: 21 (Android 5.0)
- **NDK Version**: 25b
- **Architecture**: arm64-v8a, armeabi-v7a
- **Permissions**: INTERNET

### 自定义配置

如需修改应用配置，请编辑 `buildozer.spec` 文件中的相应参数。

## 故障排除

1. **构建失败**: 检查 GitHub Actions 中的构建日志
2. **依赖问题**: 确保 `buildozer.spec` 中的 requirements 包含所需的 Python 包
3. **权限问题**: 根据应用需求在 `android.permissions` 中添加必要权限

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。