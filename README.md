# Augment Free

[English](#english) | [中文](#chinese)

# <a name="chinese"></a>中文版

Augment Free 是一个用于清理AugmentCode相关数据的工具，可以在同一台电脑上无限次登录不同的账号，避免账号被锁定。

## 功能特性

- 📝 修改Telemetry ID
  - 重置设备 ID 和机器 ID
  - 自动备份原始数据
  - 生成新的随机 ID

- 🗃️ 数据库清理
  - 清理 SQLite 数据库中的特定记录
  - 自动备份数据库文件
  - 删除包含 'augment' 关键字的记录

- 💾 工作区存储管理
  - 清理工作区存储文件
  - 自动备份工作区数据

## 安装说明

### Windows 用户（推荐）

**方式一：直接下载**
- 下载：[augment-free.exe](./augment-free.exe)
- 双击运行即可

**方式二：从 Releases 下载**
- 从 [Releases](https://github.com/yourusername/augment-free/releases) 页面下载最新版本

### 其他系统用户

1. 确保你的系统已安装 Python 3.10及以上
2. 克隆此仓库到本地：
   ```bash
   git clone https://github.com/yourusername/augment-free.git
   cd augment-free
   ```

## 使用方法

1. 退出AugmentCode插件
2. 完全退出 VS Code
3. 运行程序：

**Windows 用户：**
```bash
# 双击 augment-free.exe 或在命令行中运行
augment-free.exe
```

**其他系统用户：**
```bash
python index.py
```

4. 重新启动 VS Code
5. AugmentCode 插件中使用新的邮箱进行登录

## 项目结构

```
augment-free/
├── index.py              # 主程序入口
├── augutils/             # 工具类目录
│   ├── json_modifier.py      # JSON 文件修改工具
│   ├── sqlite_modifier.py    # SQLite 数据库修改工具
│   └── workspace_cleaner.py  # 工作区清理工具
└── utils/                # 通用工具目录
    └── paths.py             # 路径管理工具
```

## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目。

## 许可证

此项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

---

# <a name="english"></a>English Version

Augment Free is a tool for cleaning AugmentCode-related data, allowing unlimited logins with different accounts on the same computer while avoiding account lockouts.

## Features

- 📝 Telemetry ID Modification
  - Reset device ID and machine ID
  - Automatic backup of original data
  - Generate new random IDs

- 🗃️ Database Cleanup
  - Clean specific records in SQLite database
  - Automatic database file backup
  - Remove records containing 'augment' keyword

- 💾 Workspace Storage Management
  - Clean workspace storage files
  - Automatic workspace data backup

## Installation

### Windows Users (Recommended)

**Method 1: Direct Download**
- Download: [augment-free.exe](./augment-free.exe)
- Double-click to run

**Method 2: From Releases**
- Download from [Releases](https://github.com/yourusername/augment-free/releases) page

### Other Systems

1. Ensure Python 3.10 or above is installed on your system
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/augment-free.git
   cd augment-free
   ```

## Usage

1. Exit the AugmentCode plugin
2. Completely close VS Code
3. Run the program:

**Windows users:**
```bash
# Double-click augment-free.exe or run in command line
augment-free.exe
```

**Other systems:**
```bash
python index.py
```

4. Restart VS Code
5. Log in to the AugmentCode plugin with a new email

## Project Structure

```
augment-free/
├── index.py              # Main program entry
├── augutils/             # Utility classes directory
│   ├── json_modifier.py      # JSON file modification tool
│   ├── sqlite_modifier.py    # SQLite database modification tool
│   └── workspace_cleaner.py  # Workspace cleanup tool
└── utils/                # Common utilities directory
    └── paths.py             # Path management tool
```

## Contributing

Issues and Pull Requests are welcome to help improve this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 