# Augment VSCode 扩展本地存储完整清理工具 (PowerShell 版本)
# 基于对 Augment 扩展代码库的深入分析开发

param(
    [switch]$Scan,
    [switch]$Clean,
    [switch]$NoBackup,
    [string]$Restore,
    [switch]$CleanGlobal,
    [switch]$CleanWorkspace,
    [switch]$CleanSettings,
    [switch]$CleanLogs,
    [switch]$CleanCache,
    [switch]$CleanRegistry,
    [switch]$Help
)

# 全局变量
$ExtensionId = "Augment.vscode-augment"
$VSCodeDataDir = "$env:APPDATA\Code"
$BackupDir = "augment_backup\$(Get-Date -Format 'yyyyMMdd_HHmmss')"
$LogFile = "augment_cleaner.log"

# 存储路径定义
$StoragePaths = @{
    GlobalStorage = "$VSCodeDataDir\User\globalStorage\$ExtensionId"
    WorkspaceStorageRoot = "$VSCodeDataDir\User\workspaceStorage"
    UserSettings = "$VSCodeDataDir\User\settings.json"
    UserKeybindings = "$VSCodeDataDir\User\keybindings.json"
    ExtensionsDir = "$VSCodeDataDir\extensions"
    LogsDir = "$VSCodeDataDir\logs"
    CacheDir = "$VSCodeDataDir\CachedExtensions"
}

# Augment 相关的配置键
$AugmentConfigKeys = @(
    "augment.advanced.apiToken",
    "augment.enableEmptyFileHint",
    "augment.conflictingCodingAssistantCheck",
    "augment.advanced.completionURL",
    "augment.advanced.integrations"
)

# 日志函数
function Write-Log {
    param([string]$Message, [string]$Level = "INFO")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logMessage = "[$timestamp] [$Level] $Message"
    Write-Host $logMessage
    Add-Content -Path $LogFile -Value $logMessage -Encoding UTF8
}

function Show-Help {
    Write-Host @"
Augment VSCode 扩展本地存储完整清理工具 (PowerShell 版本)

用法:
    .\augment_cleaner.ps1 [参数]

参数:
    -Scan              扫描 Augment 相关数据
    -Clean             执行完整清理（自动备份）
    -NoBackup          清理时不创建备份
    -Restore <path>    从指定备份路径恢复
    -CleanGlobal       只清理全局存储
    -CleanWorkspace    只清理工作区存储
    -CleanSettings     只清理用户配置
    -CleanLogs         只清理扩展日志
    -CleanCache        只清理扩展缓存
    -CleanRegistry     只清理注册表项
    -Help              显示此帮助信息

示例:
    .\augment_cleaner.ps1 -Scan
    .\augment_cleaner.ps1 -Clean
    .\augment_cleaner.ps1 -Clean -NoBackup
    .\augment_cleaner.ps1 -Restore "augment_backup\20241201_143022"
"@
}

function Test-VSCodeRunning {
    $vscodeProcesses = Get-Process -Name "*code*" -ErrorAction SilentlyContinue
    if ($vscodeProcesses) {
        Write-Log "检测到 VSCode 正在运行，建议先关闭 VSCode 再执行清理操作" "WARNING"
        $response = Read-Host "是否继续？(y/N)"
        if ($response.ToLower() -ne 'y') {
            Write-Log "操作已取消"
            exit
        }
    }
}

function New-Backup {
    try {
        Write-Log "创建备份到: $BackupDir"
        New-Item -Path $BackupDir -ItemType Directory -Force | Out-Null
        
        # 备份全局存储
        if (Test-Path $StoragePaths.GlobalStorage) {
            $backupGlobal = Join-Path $BackupDir "globalStorage"
            Copy-Item -Path $StoragePaths.GlobalStorage -Destination $backupGlobal -Recurse -Force
            Write-Log "已备份全局存储: $backupGlobal"
        }
        
        # 备份工作区存储中的 Augment 数据
        if (Test-Path $StoragePaths.WorkspaceStorageRoot) {
            $backupWorkspace = Join-Path $BackupDir "workspaceStorage"
            New-Item -Path $backupWorkspace -ItemType Directory -Force | Out-Null
            
            Get-ChildItem -Path $StoragePaths.WorkspaceStorageRoot -Directory | ForEach-Object {
                $augmentWorkspace = Join-Path $_.FullName $ExtensionId
                if (Test-Path $augmentWorkspace) {
                    $backupPath = Join-Path $backupWorkspace $_.Name
                    New-Item -Path $backupPath -ItemType Directory -Force | Out-Null
                    Copy-Item -Path $augmentWorkspace -Destination (Join-Path $backupPath $ExtensionId) -Recurse -Force
                    Write-Log "已备份工作区存储: $backupPath"
                }
            }
        }
        
        # 备份用户配置
        if (Test-Path $StoragePaths.UserSettings) {
            $backupSettings = Join-Path $BackupDir "settings.json"
            Copy-Item -Path $StoragePaths.UserSettings -Destination $backupSettings -Force
            Write-Log "已备份用户配置: $backupSettings"
        }
        
        return $true
    }
    catch {
        Write-Log "备份失败: $($_.Exception.Message)" "ERROR"
        return $false
    }
}

function Remove-GlobalStorage {
    try {
        if (Test-Path $StoragePaths.GlobalStorage) {
            Write-Log "清理全局存储: $($StoragePaths.GlobalStorage)"
            Remove-Item -Path $StoragePaths.GlobalStorage -Recurse -Force
            Write-Log "全局存储清理完成"
            return $true
        } else {
            Write-Log "全局存储目录不存在，跳过清理"
            return $true
        }
    }
    catch {
        Write-Log "清理全局存储失败: $($_.Exception.Message)" "ERROR"
        return $false
    }
}

function Remove-WorkspaceStorage {
    try {
        if (-not (Test-Path $StoragePaths.WorkspaceStorageRoot)) {
            Write-Log "工作区存储目录不存在，跳过清理"
            return $true
        }
        
        $cleanedCount = 0
        Get-ChildItem -Path $StoragePaths.WorkspaceStorageRoot -Directory | ForEach-Object {
            $augmentWorkspace = Join-Path $_.FullName $ExtensionId
            if (Test-Path $augmentWorkspace) {
                Write-Log "清理工作区存储: $augmentWorkspace"
                Remove-Item -Path $augmentWorkspace -Recurse -Force
                $cleanedCount++
            }
        }
        
        Write-Log "工作区存储清理完成，共清理 $cleanedCount 个工作区"
        return $true
    }
    catch {
        Write-Log "清理工作区存储失败: $($_.Exception.Message)" "ERROR"
        return $false
    }
}

function Remove-UserSettings {
    try {
        if (-not (Test-Path $StoragePaths.UserSettings)) {
            Write-Log "用户配置文件不存在，跳过清理"
            return $true
        }
        
        # 读取配置文件
        $settings = Get-Content -Path $StoragePaths.UserSettings -Raw -Encoding UTF8 | ConvertFrom-Json
        
        # 移除 Augment 相关配置
        $removedKeys = @()
        $settingsHash = @{}
        
        # 转换为哈希表以便操作
        $settings.PSObject.Properties | ForEach-Object {
            $settingsHash[$_.Name] = $_.Value
        }
        
        # 检查并移除 Augment 相关键
        $settingsHash.Keys | ForEach-Object {
            $key = $_
            foreach ($augmentKey in $AugmentConfigKeys) {
                if ($key -like "*$augmentKey*") {
                    $settingsHash.Remove($key)
                    $removedKeys += $key
                    break
                }
            }
        }
        
        if ($removedKeys.Count -gt 0) {
            # 写回配置文件
            $settingsHash | ConvertTo-Json -Depth 10 | Set-Content -Path $StoragePaths.UserSettings -Encoding UTF8
            Write-Log "用户配置清理完成，移除了 $($removedKeys.Count) 个配置项: $($removedKeys -join ', ')"
        } else {
            Write-Log "用户配置中未找到 Augment 相关配置"
        }
        
        return $true
    }
    catch {
        Write-Log "清理用户配置失败: $($_.Exception.Message)" "ERROR"
        return $false
    }
}

function Remove-ExtensionLogs {
    try {
        if (-not (Test-Path $StoragePaths.LogsDir)) {
            Write-Log "日志目录不存在，跳过清理"
            return $true
        }
        
        $cleanedCount = 0
        Get-ChildItem -Path $StoragePaths.LogsDir -Recurse -File | Where-Object { $_.Name -like "*augment*" } | ForEach-Object {
            Write-Log "清理日志文件: $($_.FullName)"
            Remove-Item -Path $_.FullName -Force
            $cleanedCount++
        }
        
        Write-Log "扩展日志清理完成，共清理 $cleanedCount 个日志文件"
        return $true
    }
    catch {
        Write-Log "清理扩展日志失败: $($_.Exception.Message)" "ERROR"
        return $false
    }
}

function Remove-ExtensionCache {
    try {
        if (-not (Test-Path $StoragePaths.CacheDir)) {
            Write-Log "缓存目录不存在，跳过清理"
            return $true
        }
        
        $cleanedCount = 0
        Get-ChildItem -Path $StoragePaths.CacheDir -Recurse | Where-Object { $_.Name -like "*augment*" } | ForEach-Object {
            Write-Log "清理缓存项: $($_.FullName)"
            Remove-Item -Path $_.FullName -Recurse -Force
            $cleanedCount++
        }
        
        Write-Log "扩展缓存清理完成，共清理 $cleanedCount 个缓存项"
        return $true
    }
    catch {
        Write-Log "清理扩展缓存失败: $($_.Exception.Message)" "ERROR"
        return $false
    }
}

function Remove-RegistryEntries {
    try {
        $registryPaths = @(
            "HKCU:\SOFTWARE\Microsoft\VSCode\Extensions",
            "HKCU:\SOFTWARE\Classes\VSCode"
        )
        
        $cleanedCount = 0
        foreach ($regPath in $registryPaths) {
            if (Test-Path $regPath) {
                Get-ChildItem -Path $regPath -ErrorAction SilentlyContinue | Where-Object { $_.Name -like "*augment*" } | ForEach-Object {
                    Write-Log "清理注册表项: $($_.Name)"
                    Remove-Item -Path $_.PSPath -Recurse -Force
                    $cleanedCount++
                }
            }
        }
        
        Write-Log "注册表清理完成，共清理 $cleanedCount 项"
        return $true
    }
    catch {
        Write-Log "清理注册表失败: $($_.Exception.Message)" "ERROR"
        return $false
    }
}

function Get-AugmentData {
    Write-Log "开始扫描 Augment 相关数据..."

    $foundData = @{
        GlobalStorage = @()
        WorkspaceStorage = @()
        UserSettings = @()
        Logs = @()
        Cache = @()
        Registry = @()
    }

    # 扫描全局存储
    if (Test-Path $StoragePaths.GlobalStorage) {
        $foundData.GlobalStorage = Get-ChildItem -Path $StoragePaths.GlobalStorage -Recurse | ForEach-Object { $_.FullName }
    }

    # 扫描工作区存储
    if (Test-Path $StoragePaths.WorkspaceStorageRoot) {
        Get-ChildItem -Path $StoragePaths.WorkspaceStorageRoot -Directory | ForEach-Object {
            $augmentWorkspace = Join-Path $_.FullName $ExtensionId
            if (Test-Path $augmentWorkspace) {
                $foundData.WorkspaceStorage += Get-ChildItem -Path $augmentWorkspace -Recurse | ForEach-Object { $_.FullName }
            }
        }
    }

    # 扫描用户配置
    if (Test-Path $StoragePaths.UserSettings) {
        try {
            $settings = Get-Content -Path $StoragePaths.UserSettings -Raw -Encoding UTF8 | ConvertFrom-Json
            $settings.PSObject.Properties | ForEach-Object {
                foreach ($augmentKey in $AugmentConfigKeys) {
                    if ($_.Name -like "*$augmentKey*") {
                        $foundData.UserSettings += "$($_.Name): $($_.Value)"
                        break
                    }
                }
            }
        }
        catch {
            Write-Log "扫描用户配置时出错: $($_.Exception.Message)" "WARNING"
        }
    }

    # 扫描日志
    if (Test-Path $StoragePaths.LogsDir) {
        $foundData.Logs = Get-ChildItem -Path $StoragePaths.LogsDir -Recurse -File | Where-Object { $_.Name -like "*augment*" } | ForEach-Object { $_.FullName }
    }

    # 扫描缓存
    if (Test-Path $StoragePaths.CacheDir) {
        $foundData.Cache = Get-ChildItem -Path $StoragePaths.CacheDir -Recurse | Where-Object { $_.Name -like "*augment*" } | ForEach-Object { $_.FullName }
    }

    return $foundData
}

function Show-ScanResults {
    param($FoundData)

    Write-Log "=== Augment 数据扫描结果 ==="

    $totalItems = 0
    foreach ($category in $FoundData.Keys) {
        $items = $FoundData[$category]
        if ($items.Count -gt 0) {
            Write-Log "`n$($category.ToUpper()) ($($items.Count) 项):"
            $displayItems = $items | Select-Object -First 10
            foreach ($item in $displayItems) {
                Write-Log "  - $item"
            }
            if ($items.Count -gt 10) {
                Write-Log "  ... 还有 $($items.Count - 10) 项"
            }
            $totalItems += $items.Count
        } else {
            Write-Log "`n$($category.ToUpper()): 未找到相关数据"
        }
    }

    Write-Log "`n总计找到 $totalItems 项 Augment 相关数据"
}

function Invoke-FullClean {
    param([bool]$CreateBackup = $true)

    Write-Log "开始执行 Augment 扩展完整清理..."

    # 创建备份
    if ($CreateBackup) {
        if (-not (New-Backup)) {
            Write-Log "备份失败，终止清理操作" "ERROR"
            return $false
        }
    }

    # 执行各项清理
    $success = $true

    $success = $success -and (Remove-GlobalStorage)
    $success = $success -and (Remove-WorkspaceStorage)
    $success = $success -and (Remove-UserSettings)
    $success = $success -and (Remove-ExtensionLogs)
    $success = $success -and (Remove-ExtensionCache)
    $success = $success -and (Remove-RegistryEntries)

    if ($success) {
        Write-Log "✅ Augment 扩展完整清理成功完成！"
    } else {
        Write-Log "❌ 清理过程中出现错误，请检查日志" "ERROR"
    }

    return $success
}

function Restore-FromBackup {
    param([string]$BackupPath)

    try {
        if (-not (Test-Path $BackupPath)) {
            Write-Log "备份目录不存在: $BackupPath" "ERROR"
            return $false
        }

        Write-Log "从备份恢复: $BackupPath"

        # 恢复全局存储
        $backupGlobal = Join-Path $BackupPath "globalStorage"
        if (Test-Path $backupGlobal) {
            if (Test-Path $StoragePaths.GlobalStorage) {
                Remove-Item -Path $StoragePaths.GlobalStorage -Recurse -Force
            }
            Copy-Item -Path $backupGlobal -Destination $StoragePaths.GlobalStorage -Recurse -Force
            Write-Log "已恢复全局存储"
        }

        # 恢复工作区存储
        $backupWorkspace = Join-Path $BackupPath "workspaceStorage"
        if (Test-Path $backupWorkspace) {
            Get-ChildItem -Path $backupWorkspace -Directory | ForEach-Object {
                $targetWorkspace = Join-Path $StoragePaths.WorkspaceStorageRoot $_.Name $ExtensionId
                if (Test-Path $targetWorkspace) {
                    Remove-Item -Path $targetWorkspace -Recurse -Force
                }
                $sourceWorkspace = Join-Path $_.FullName $ExtensionId
                if (Test-Path $sourceWorkspace) {
                    New-Item -Path (Split-Path $targetWorkspace) -ItemType Directory -Force | Out-Null
                    Copy-Item -Path $sourceWorkspace -Destination $targetWorkspace -Recurse -Force
                    Write-Log "已恢复工作区存储: $($_.Name)"
                }
            }
        }

        # 恢复用户配置
        $backupSettings = Join-Path $BackupPath "settings.json"
        if (Test-Path $backupSettings) {
            Copy-Item -Path $backupSettings -Destination $StoragePaths.UserSettings -Force
            Write-Log "已恢复用户配置"
        }

        Write-Log "✅ 从备份恢复成功完成！"
        return $true
    }
    catch {
        Write-Log "从备份恢复失败: $($_.Exception.Message)" "ERROR"
        return $false
    }
}

# 主程序逻辑
if ($Help) {
    Show-Help
    exit
}

# 检查 VSCode 是否在运行
Test-VSCodeRunning

# 执行相应操作
if ($Scan) {
    $foundData = Get-AugmentData
    Show-ScanResults $foundData
}
elseif ($Clean) {
    $createBackup = -not $NoBackup
    $success = Invoke-FullClean $createBackup
    if ($success) {
        Write-Log "清理完成！重启 VSCode 后 Augment 扩展将处于全新状态"
    } else {
        Write-Log "清理过程中出现错误，请检查日志文件" "ERROR"
    }
}
elseif ($Restore) {
    $success = Restore-FromBackup $Restore
    if ($success) {
        Write-Log "恢复完成！重启 VSCode 后 Augment 扩展将恢复到备份状态"
    } else {
        Write-Log "恢复过程中出现错误，请检查日志文件" "ERROR"
    }
}
elseif ($CleanGlobal) {
    Remove-GlobalStorage
}
elseif ($CleanWorkspace) {
    Remove-WorkspaceStorage
}
elseif ($CleanSettings) {
    Remove-UserSettings
}
elseif ($CleanLogs) {
    Remove-ExtensionLogs
}
elseif ($CleanCache) {
    Remove-ExtensionCache
}
elseif ($CleanRegistry) {
    Remove-RegistryEntries
}
else {
    Show-Help
}
