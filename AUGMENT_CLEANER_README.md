# Augment VSCode 扩展本地存储完整清理工具

基于对 Augment VSCode 扩展代码库的深入分析开发的专业清理工具，能够完整、系统地清理 Augment 扩展的所有本地存储数据。

## 🎯 功能特性

### ✅ **完整清理覆盖**
- **VSCode 扩展全局存储** (`globalStorage`)
- **工作区存储** (`workspaceStorage`) 
- **用户配置文件** (`settings.json`)
- **扩展日志文件**
- **扩展缓存数据**
- **SQLite 数据库存储**
- **Windows 注册表项**

### 🛡️ **安全保障**
- **自动备份**: 清理前自动创建完整备份
- **恢复功能**: 支持从备份完整恢复
- **进程检测**: 自动检测 VSCode 运行状态
- **详细日志**: 完整的操作日志记录

### 🔧 **灵活操作**
- **扫描模式**: 仅扫描不清理，查看存储数据
- **选择性清理**: 支持单独清理特定类型数据
- **批量清理**: 一键完整清理所有数据
- **跨平台支持**: Windows/macOS/Linux

## 📊 **基于代码分析的存储位置**

通过对 Augment 扩展源码的深入分析，我们发现了以下关键存储机制：

### **1. 全局存储 (GlobalState)**
```javascript
// 从 out/extension.js 分析得出
async getValue(extensionId, key, scope) {
    return await this._extensionContext.globalState.get(this.getKey(extensionId, key));
}

getKey(extensionId, key) {
    return ["sidecar", extensionId, key].join(".");
}
```

**存储路径**: `%APPDATA%\Code\User\globalStorage\Augment.vscode-augment\`

**存储内容**:
- `sidecar.Augment.vscode-augment.*` 键值
- `hasEverUsedAgent` 试用状态标记
- `userTier` 用户层级信息
- `sessionId` 会话标识符
- `apiToken` 认证令牌

### **2. 工作区存储 (WorkspaceStorage)**
```json
// 从 package.json 分析得出
"filenamePattern": "**/workspaceStorage/*/Augment.vscode-augment/Augment-Memories"
```

**存储路径**: `%APPDATA%\Code\User\workspaceStorage\{workspace-id}\Augment.vscode-augment\`

**存储内容**:
- `Augment-Memories` 记忆文件
- 工作区特定的配置和状态

### **3. 用户配置存储**
```json
// 从 package.json 分析得出
"augment.advanced": {
    "properties": {
        "apiToken": {
            "type": "string",
            "description": "API token for Augment access."
        }
    }
}
```

**存储路径**: `%APPDATA%\Code\User\settings.json`

**配置键**:
- `augment.advanced.apiToken`
- `augment.enableEmptyFileHint`
- `augment.conflictingCodingAssistantCheck`
- `augment.advanced.completionURL`
- `augment.advanced.integrations`

## 🚀 **使用方法**

### **Python 版本**

#### **安装依赖**
```bash
pip install psutil  # 可选，用于进程检测
```

#### **基本用法**
```bash
# 扫描 Augment 数据
python augment_cleaner.py --scan

# 完整清理（自动备份）
python augment_cleaner.py --clean

# 完整清理（不备份）
python augment_cleaner.py --clean --no-backup

# 从备份恢复
python augment_cleaner.py --restore "augment_backup/20241201_143022"

# 选择性清理
python augment_cleaner.py --clean-global      # 只清理全局存储
python augment_cleaner.py --clean-workspace   # 只清理工作区存储
python augment_cleaner.py --clean-settings    # 只清理用户配置
```

### **PowerShell 版本**

#### **基本用法**
```powershell
# 扫描 Augment 数据
.\augment_cleaner.ps1 -Scan

# 完整清理（自动备份）
.\augment_cleaner.ps1 -Clean

# 完整清理（不备份）
.\augment_cleaner.ps1 -Clean -NoBackup

# 从备份恢复
.\augment_cleaner.ps1 -Restore "augment_backup\20241201_143022"

# 选择性清理
.\augment_cleaner.ps1 -CleanGlobal      # 只清理全局存储
.\augment_cleaner.ps1 -CleanWorkspace   # 只清理工作区存储
.\augment_cleaner.ps1 -CleanSettings    # 只清理用户配置
```

## 📋 **操作步骤**

### **1. 准备工作**
1. **关闭 VSCode**: 确保所有 VSCode 窗口已关闭
2. **下载工具**: 下载 `augment_cleaner.py` 或 `augment_cleaner.ps1`
3. **管理员权限**: 建议以管理员权限运行（用于注册表清理）

### **2. 扫描数据**
```bash
python augment_cleaner.py --scan
```
这将显示所有找到的 Augment 相关数据，不会进行任何删除操作。

### **3. 执行清理**
```bash
python augment_cleaner.py --clean
```
这将：
- 自动创建备份到 `augment_backup/` 目录
- 清理所有 Augment 相关数据
- 生成详细的操作日志

### **4. 验证结果**
1. 重新启动 VSCode
2. 检查 Augment 扩展状态
3. 确认试用限制已重置

### **5. 恢复（如需要）**
```bash
python augment_cleaner.py --restore "augment_backup/20241201_143022"
```

## 📁 **文件结构**

```
augment_cleaner/
├── augment_cleaner.py          # Python 版本清理工具
├── augment_cleaner.ps1         # PowerShell 版本清理工具
├── AUGMENT_CLEANER_README.md   # 使用说明文档
├── augment_cleaner.log         # 操作日志文件
└── augment_backup/             # 备份目录
    └── 20241201_143022/        # 时间戳命名的备份
        ├── globalStorage/      # 全局存储备份
        ├── workspaceStorage/   # 工作区存储备份
        └── settings.json       # 用户配置备份
```

## ⚠️ **重要提醒**

### **法律和伦理考虑**
- 此工具仅用于**学习和研究目的**
- 使用前请确保符合软件许可协议
- 建议购买正版 Augment Professional 授权
- 不建议用于商业环境或生产用途

### **技术风险**
- 清理操作不可逆，请务必先备份
- 可能影响其他 VSCode 扩展的正常使用
- 建议在测试环境中先行验证

### **使用限制**
- 需要管理员权限（用于注册表操作）
- 仅支持标准 VSCode 安装路径
- 不支持便携版或自定义安装路径

## 🔧 **技术实现**

### **核心技术**
- **存储路径分析**: 基于 VSCode 扩展 API 规范
- **数据结构解析**: 深入分析 Augment 存储格式
- **安全备份机制**: 完整的数据备份和恢复
- **跨平台兼容**: 支持 Windows/macOS/Linux

### **代码质量**
- **类型注解**: 完整的 Python 类型提示
- **错误处理**: 全面的异常捕获和处理
- **日志记录**: 详细的操作日志和状态跟踪
- **代码注释**: 清晰的中文注释和文档

## 📞 **支持和反馈**

如果在使用过程中遇到问题或有改进建议，请：

1. 检查操作日志文件 `augment_cleaner.log`
2. 确认 VSCode 已完全关闭
3. 验证是否有足够的系统权限
4. 检查备份文件是否完整

## 📄 **许可证**

本工具基于 MIT 许可证开源，仅供学习和研究使用。使用者需自行承担使用风险，并确保遵守相关法律法规和软件许可协议。
