# 快速开始 - Augment Free

## 🎯 Windows 用户（推荐）

### 1. 下载 exe 文件
- 访问 [Releases](https://github.com/yourusername/augment-free/releases) 页面
- 下载最新的 `augment-free.exe`

### 2. 使用步骤
1. **完全退出 VS Code** （重要！）
2. **双击运行** `augment-free.exe`
3. **等待程序完成** 所有操作
4. **重启 VS Code**
5. **使用新邮箱登录** AugmentCode

### 3. 注意事项
- ✅ 程序会自动备份原始文件
- ✅ 支持 Windows 10/11
- ✅ 无需安装 Python
- ⚠️ 必须完全关闭 VS Code 后运行

---

## 🛠️ 开发者/高级用户

### 从源码运行

```bash
# 克隆项目
git clone https://github.com/yourusername/augment-free.git
cd augment-free

# 直接运行
python index.py
```

### 自己构建 exe

```bash
# 安装构建工具
pip install pyinstaller

# 快速构建
python build.py

# 或使用批处理（Windows）
build.bat
```

---

## 🔧 故障排除

### 常见问题

**Q: 程序运行后没有效果？**
A: 确保完全关闭了 VS Code，包括所有窗口和后台进程

**Q: 提示文件不存在？**
A: 确保 VS Code 已经运行过至少一次，生成了配置文件

**Q: 备份文件在哪里？**
A: 程序会显示备份文件的完整路径，通常在原文件旁边

**Q: 如何恢复原始设置？**
A: 使用程序生成的备份文件覆盖对应的原文件

### 获取帮助

- 📖 查看 [完整文档](README.md)
- 🐛 报告问题：[GitHub Issues](https://github.com/yourusername/augment-free/issues)
- 💬 讨论交流：[GitHub Discussions](https://github.com/yourusername/augment-free/discussions)

---

## 📋 支持的系统

| 系统 | 支持状态 | 说明 |
|------|----------|------|
| Windows 10/11 | ✅ 完全支持 | 推荐使用 exe 文件 |
| macOS | ✅ 源码运行 | 需要 Python 3.10+ |
| Linux | ✅ 源码运行 | 需要 Python 3.10+ |

---

## 🚀 一键使用（Windows）

1. 下载 `augment-free.exe`
2. 关闭 VS Code
3. 双击运行
4. 重启 VS Code
5. 新邮箱登录

就这么简单！🎉
