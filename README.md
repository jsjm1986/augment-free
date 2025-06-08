<div align="center">

# 🚀 Augment Free

**一键重置 AugmentCode 数据，轻松切换账号**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue.svg)](https://github.com/yourusername/augment-free)
[![Version](https://img.shields.io/badge/Version-v1.0.0-green.svg)](https://github.com/yourusername/augment-free/releases)

[🇺🇸 English](#english) | [🇨🇳 中文](#chinese)

</div>

---

# <a name="chinese"></a>🇨🇳 中文版

## 📖 项目简介

**Augment Free** 是一个专为 AugmentCode 用户设计的数据清理工具，帮助您在同一台电脑上无限次切换不同账号，彻底解决账号被锁定的问题。

### 🎯 解决的问题
- ❌ AugmentCode 限制同一设备只能使用一个账号
- ❌ 切换账号时出现"设备已绑定"错误
- ❌ 无法在团队中共享设备使用不同账号
- ❌ 试用期结束后无法使用新账号

### ✅ 我们的解决方案
- ✅ **一键重置**：自动清理所有相关数据
- ✅ **安全备份**：操作前自动备份原始文件
- ✅ **跨平台支持**：Windows/macOS/Linux 全平台兼容
- ✅ **零配置使用**：Windows 用户双击即用，无需安装

## ⭐ 核心功能

<table>
<tr>
<td width="50%">

### 🔑 身份重置
- **设备 ID 重置**：生成全新的设备标识
- **机器 ID 重置**：更新机器唯一标识
- **遥测数据清理**：清除所有追踪数据
- **加密安全**：使用密码学安全的随机数生成

</td>
<td width="50%">

### 🗄️ 数据清理
- **数据库清理**：自动清理 SQLite 数据库记录
- **工作区清理**：清除工作区存储文件
- **缓存清理**：删除所有相关缓存数据
- **智能识别**：精准定位 AugmentCode 相关数据

</td>
</tr>
<tr>
<td width="50%">

### 🛡️ 安全保障
- **自动备份**：操作前备份所有原始文件
- **一键恢复**：支持快速恢复到原始状态
- **操作日志**：详细记录所有操作过程
- **错误处理**：完善的异常处理机制

</td>
<td width="50%">

### 🌍 跨平台支持
- **Windows**：提供独立 exe 文件，双击即用
- **macOS**：完美支持 Apple Silicon 和 Intel
- **Linux**：支持所有主流发行版
- **路径智能**：自动识别不同系统的配置路径

</td>
</tr>
</table>

## 📥 快速开始

### 🪟 Windows 用户（推荐）

<div align="center">

**🎉 零配置，开箱即用！**

[![Download](https://img.shields.io/badge/下载-augment--free.exe-blue?style=for-the-badge&logo=windows)](./augment-free.exe)

</div>

**方式一：直接下载（推荐）**
```
1. 点击上方按钮下载 augment-free.exe
2. 双击运行，无需安装任何依赖
3. 文件大小：9.3 MB
```

**方式二：从 Releases 下载**
```
访问 GitHub Releases 页面获取最新版本
包含完整的发布说明和更新日志
```

### 🍎 macOS / 🐧 Linux 用户

**系统要求**
- Python 3.10 或更高版本
- Git（用于克隆仓库）

**安装步骤**
```bash
# 1. 克隆仓库
git clone https://github.com/yourusername/augment-free.git
cd augment-free

# 2. 直接运行（无需安装依赖）
python index.py
```

> 💡 **提示**：本项目仅使用 Python 标准库，无需安装额外依赖包

## 🚀 使用指南

### 📋 操作步骤

<div align="center">

**🔄 五步完成账号切换**

```
🔴 步骤1    🟠 步骤2    🟢 步骤3    🔵 步骤4    🟣 步骤5
   ↓         ↓         ↓         ↓         ↓
退出插件 → 关闭VS Code → 运行工具 → 重启VS Code → 新账号登录
```

</div>

#### 🔴 步骤 1：退出 AugmentCode 插件
```
在 VS Code 中禁用或卸载 AugmentCode 插件
确保插件完全停止运行
```

#### 🟠 步骤 2：完全关闭 VS Code
```
关闭所有 VS Code 窗口
检查任务管理器，确保没有 Code.exe 进程
```

#### 🟢 步骤 3：运行清理工具

**🪟 Windows 用户**
```bash
# 方式一：双击运行（推荐）
双击 augment-free.exe

# 方式二：命令行运行
.\augment-free.exe
```

**🍎 macOS / 🐧 Linux 用户**
```bash
python index.py
```

#### 🔵 步骤 4：重新启动 VS Code
```
等待工具运行完成
重新打开 VS Code
```

#### 🟣 步骤 5：登录新账号
```
重新安装或启用 AugmentCode 插件
使用新的邮箱账号登录
享受全新的使用体验！
```

### 📊 运行示例

程序运行时会显示详细的操作信息：

```
System Paths:
Home Directory: C:\Users\username
App Data Directory: C:\Users\username\AppData\Roaming
Storage Path: C:\Users\username\AppData\Roaming\Code\User\globalStorage\storage.json
...

Modifying Telemetry IDs:
✅ Backup created at: storage.json.bak.1749364690
✅ Old Machine ID: 0dffa52e5eddc4b4652984d03218ff310e8f066de5bc8c01a167f4d12037faa2
✅ New Machine ID: b4371542c0a2f70b2501a181f2a524a2e5dd7f072e79e0feb74065b4603dac92
...

🎉 Now you can run VS Code and login with the new email.
```

## ⚠️ 重要提醒

<div align="center">

| ⚠️ 注意事项 | 📝 说明 |
|------------|---------|
| **备份数据** | 程序会自动备份，但建议手动备份重要数据 |
| **关闭 VS Code** | 必须完全关闭 VS Code 才能正常运行 |
| **管理员权限** | 某些情况下可能需要管理员权限 |
| **网络连接** | 首次登录新账号时需要网络连接 |

</div>

## 🔧 故障排除

<details>
<summary><b>🔍 常见问题解答</b></summary>

### Q: 程序运行后没有效果？
**A:** 确保完全关闭了 VS Code，包括所有窗口和后台进程。可以通过任务管理器检查是否还有 `Code.exe` 进程。

### Q: 提示"文件不存在"错误？
**A:** 确保 VS Code 已经运行过至少一次，生成了必要的配置文件。如果是全新安装的 VS Code，请先运行一次。

### Q: 如何恢复到原始状态？
**A:** 程序会自动创建备份文件（带时间戳），找到对应的备份文件，删除当前文件，将备份文件重命名即可。

### Q: 支持哪些版本的 VS Code？
**A:** 支持所有现代版本的 VS Code，包括 VS Code、VS Code Insiders 和 VSCodium。

### Q: 会影响其他 VS Code 插件吗？
**A:** 不会。本工具只清理 AugmentCode 相关数据，不会影响其他插件的配置和数据。

</details>

## 📊 技术规格

<table>
<tr>
<td width="50%">

### 🔧 系统要求
- **Windows**: 10/11 (x64)
- **macOS**: 10.14+ (Intel/Apple Silicon)
- **Linux**: 主流发行版 (x64)
- **Python**: 3.10+ (源码运行)

</td>
<td width="50%">

### 📦 文件信息
- **exe 大小**: 9.3 MB
- **依赖**: 无（Windows exe）
- **语言**: Python 3
- **架构**: 跨平台

</td>
</tr>
</table>

## 🏗️ 项目结构

```
augment-free/
├── 📄 augment-free.exe      # Windows 可执行文件
├── 🐍 index.py              # 主程序入口
├── 📚 README.md             # 项目文档
├── 📜 LICENSE               # MIT 许可证
├── 🚀 QUICKSTART.md         # 快速开始指南
├── 📋 RELEASE_NOTES.md      # 发布说明
├── 📁 augutils/             # 核心功能模块
│   ├── 🔧 json_modifier.py      # JSON 文件修改
│   ├── 🗄️ sqlite_modifier.py    # 数据库清理
│   └── 💾 workspace_cleaner.py  # 工作区清理
└── 📁 utils/                # 工具模块
    ├── 🔑 device_codes.py       # 设备 ID 生成
    └── 📍 paths.py              # 路径管理
```

## 🤝 参与贡献

我们欢迎所有形式的贡献！

### 🐛 报告问题
- 使用 [GitHub Issues](https://github.com/yourusername/augment-free/issues) 报告 bug
- 提供详细的错误信息和复现步骤
- 包含系统信息和 VS Code 版本

### 💡 功能建议
- 在 [GitHub Discussions](https://github.com/yourusername/augment-free/discussions) 中讨论新功能
- 详细描述功能需求和使用场景

### 🔧 代码贡献
1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 感谢所有贡献者的支持
- 感谢 VS Code 和 AugmentCode 团队
- 感谢开源社区的无私奉献

---

# <a name="english"></a>🇺🇸 English Version

## 📖 About

**Augment Free** is a powerful data cleaning tool designed specifically for AugmentCode users. It enables unlimited account switching on the same device by completely resetting device fingerprints and clearing all tracking data.

### 🎯 Problems We Solve
- ❌ AugmentCode restricts one account per device
- ❌ "Device already bound" errors when switching accounts
- ❌ Unable to share devices across team members
- ❌ Cannot use new accounts after trial expiration

### ✅ Our Solution
- ✅ **One-Click Reset**: Automatically clean all related data
- ✅ **Safe Backup**: Auto-backup original files before operations
- ✅ **Cross-Platform**: Windows/macOS/Linux full compatibility
- ✅ **Zero Configuration**: Windows users can run directly, no installation required

## ⭐ Key Features

<table>
<tr>
<td width="50%">

### 🔑 Identity Reset
- **Device ID Reset**: Generate brand new device identifiers
- **Machine ID Reset**: Update machine unique identifiers
- **Telemetry Cleanup**: Clear all tracking data
- **Cryptographically Secure**: Use cryptographic secure random generation

</td>
<td width="50%">

### 🗄️ Data Cleaning
- **Database Cleanup**: Auto-clean SQLite database records
- **Workspace Cleanup**: Clear workspace storage files
- **Cache Cleanup**: Remove all related cache data
- **Smart Detection**: Precisely locate AugmentCode-related data

</td>
</tr>
<tr>
<td width="50%">

### 🛡️ Safety Features
- **Auto Backup**: Backup all original files before operations
- **One-Click Recovery**: Support quick recovery to original state
- **Operation Logs**: Detailed logging of all operations
- **Error Handling**: Comprehensive exception handling mechanism

</td>
<td width="50%">

### 🌍 Cross-Platform Support
- **Windows**: Standalone exe file, double-click to run
- **macOS**: Perfect support for Apple Silicon and Intel
- **Linux**: Support all mainstream distributions
- **Smart Paths**: Auto-detect configuration paths for different systems

</td>
</tr>
</table>

## 📥 Quick Start

### 🪟 Windows Users (Recommended)

<div align="center">

**🎉 Zero Configuration, Ready to Use!**

[![Download](https://img.shields.io/badge/Download-augment--free.exe-blue?style=for-the-badge&logo=windows)](./augment-free.exe)

</div>

**Method 1: Direct Download (Recommended)**
```
1. Click the button above to download augment-free.exe
2. Double-click to run, no dependencies required
3. File size: 9.3 MB
```

**Method 2: From Releases**
```
Visit GitHub Releases page for the latest version
Includes complete release notes and changelog
```

### 🍎 macOS / 🐧 Linux Users

**System Requirements**
- Python 3.10 or higher
- Git (for cloning repository)

**Installation Steps**
```bash
# 1. Clone repository
git clone https://github.com/yourusername/augment-free.git
cd augment-free

# 2. Run directly (no dependencies needed)
python index.py
```

> 💡 **Tip**: This project only uses Python standard library, no additional packages required

## 🚀 Usage Guide

### 📋 Step-by-Step Instructions

#### 🔴 Step 1: Exit AugmentCode Plugin
```
Disable or uninstall AugmentCode plugin in VS Code
Ensure the plugin is completely stopped
```

#### 🟠 Step 2: Completely Close VS Code
```
Close all VS Code windows
Check Task Manager to ensure no Code.exe processes
```

#### 🟢 Step 3: Run Cleaning Tool

**🪟 Windows Users**
```bash
# Method 1: Double-click (Recommended)
Double-click augment-free.exe

# Method 2: Command line
.\augment-free.exe
```

**🍎 macOS / 🐧 Linux Users**
```bash
python index.py
```

#### 🔵 Step 4: Restart VS Code
```
Wait for the tool to complete
Reopen VS Code
```

#### 🟣 Step 5: Login with New Account
```
Reinstall or enable AugmentCode plugin
Login with a new email account
Enjoy your fresh experience!
```

### 📊 Example Output

The program displays detailed operation information:

```
System Paths:
Home Directory: /Users/username
App Data Directory: /Users/username/Library/Application Support
...

Modifying Telemetry IDs:
✅ Backup created at: storage.json.bak.1749364690
✅ Old Machine ID: 0dffa52e5eddc4b4652984d03218ff310e8f066de5bc8c01a167f4d12037faa2
✅ New Machine ID: b4371542c0a2f70b2501a181f2a524a2e5dd7f072e79e0feb74065b4603dac92
...

🎉 Now you can run VS Code and login with the new email.
```

## ⚠️ Important Notes

<div align="center">

| ⚠️ Notice | 📝 Description |
|-----------|----------------|
| **Backup Data** | Auto-backup is provided, but manual backup is recommended |
| **Close VS Code** | Must completely close VS Code for proper operation |
| **Admin Rights** | May require administrator privileges in some cases |
| **Network Connection** | Internet required for first login with new account |

</div>

## 🔧 Troubleshooting

<details>
<summary><b>🔍 Frequently Asked Questions</b></summary>

### Q: Program runs but has no effect?
**A:** Ensure VS Code is completely closed, including all windows and background processes. Check Task Manager for any remaining `Code.exe` processes.

### Q: "File not found" error?
**A:** Ensure VS Code has been run at least once to generate necessary configuration files. For fresh VS Code installations, run it once first.

### Q: How to restore to original state?
**A:** The program automatically creates backup files (with timestamps). Find the corresponding backup file, delete the current file, and rename the backup file.

### Q: Which VS Code versions are supported?
**A:** Supports all modern versions of VS Code, including VS Code, VS Code Insiders, and VSCodium.

### Q: Will it affect other VS Code extensions?
**A:** No. This tool only cleans AugmentCode-related data and won't affect other extensions' configurations and data.

</details>

## 📊 Technical Specifications

<table>
<tr>
<td width="50%">

### 🔧 System Requirements
- **Windows**: 10/11 (x64)
- **macOS**: 10.14+ (Intel/Apple Silicon)
- **Linux**: Mainstream distributions (x64)
- **Python**: 3.10+ (for source code)

</td>
<td width="50%">

### 📦 File Information
- **exe Size**: 9.3 MB
- **Dependencies**: None (Windows exe)
- **Language**: Python 3
- **Architecture**: Cross-platform

</td>
</tr>
</table>

## 🏗️ Project Structure

```
augment-free/
├── 📄 augment-free.exe      # Windows executable
├── 🐍 index.py              # Main program entry
├── 📚 README.md             # Project documentation
├── 📜 LICENSE               # MIT license
├── 🚀 QUICKSTART.md         # Quick start guide
├── 📋 RELEASE_NOTES.md      # Release notes
├── 📁 augutils/             # Core functionality modules
│   ├── 🔧 json_modifier.py      # JSON file modification
│   ├── 🗄️ sqlite_modifier.py    # Database cleanup
│   └── 💾 workspace_cleaner.py  # Workspace cleanup
└── 📁 utils/                # Utility modules
    ├── 🔑 device_codes.py       # Device ID generation
    └── 📍 paths.py              # Path management
```

## 🤝 Contributing

We welcome all forms of contributions!

### 🐛 Report Issues
- Use [GitHub Issues](https://github.com/yourusername/augment-free/issues) to report bugs
- Provide detailed error information and reproduction steps
- Include system information and VS Code version

### 💡 Feature Suggestions
- Discuss new features in [GitHub Discussions](https://github.com/yourusername/augment-free/discussions)
- Describe feature requirements and use cases in detail

### 🔧 Code Contributions
1. Fork this repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors for their support
- Thanks to VS Code and AugmentCode teams
- Thanks to the open source community for their selfless dedication

---

<div align="center">

**⭐ If this project helped you, please give it a star! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/augment-free?style=social)](https://github.com/yourusername/augment-free/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/augment-free?style=social)](https://github.com/yourusername/augment-free/network)

Made with ❤️ by the Augment Free team

</div>