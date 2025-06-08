# Augment Free v1.0.0 发布说明

## 🎉 首次正式发布

Augment Free 是一个用于清理 AugmentCode 相关数据的工具，允许在同一台电脑上无限次登录不同的账号，避免账号被锁定。

## ✨ 主要功能

- **📝 Telemetry ID 修改**
  - 重置设备 ID 和机器 ID
  - 自动备份原始数据
  - 生成新的随机 ID

- **🗃️ 数据库清理**
  - 清理 SQLite 数据库中的特定记录
  - 自动备份数据库文件
  - 删除包含 'augment' 关键字的记录

- **💾 工作区存储管理**
  - 清理工作区存储文件
  - 自动备份工作区数据

## 🚀 快速开始

### Windows 用户
1. 下载 `augment-free.exe`
2. 完全退出 VS Code
3. 双击运行 exe 文件
4. 重启 VS Code
5. 使用新邮箱登录 AugmentCode

### 其他系统用户
1. 确保安装 Python 3.10+
2. 运行 `python index.py`

## 📋 支持的系统

- ✅ Windows 10/11 (exe 文件)
- ✅ macOS (源码运行)
- ✅ Linux (源码运行)

## 🔒 安全特性

- 自动备份所有修改的文件
- 使用加密安全的随机数生成
- 跨平台路径处理
- 错误处理和恢复机制

## 📦 文件信息

- **exe 文件大小**: 9.3 MB
- **依赖**: 无需额外安装
- **Python 版本**: 3.10+ (仅源码运行需要)

## 🐛 已知问题

- 无已知问题

## 📞 支持

- 项目地址: https://github.com/yourusername/augment-free
- 问题反馈: https://github.com/yourusername/augment-free/issues
- 讨论交流: https://github.com/yourusername/augment-free/discussions

---

**注意**: 使用前请确保完全退出 VS Code，程序会自动备份所有原始文件。
