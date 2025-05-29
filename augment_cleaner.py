#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Augment VSCode 扩展本地存储完整清理工具
基于对 Augment 扩展代码库的深入分析开发

功能：
- 清理 VSCode 扩展全局存储
- 清理工作区存储
- 清理用户配置
- 清理缓存和临时文件
- 备份和恢复功能
"""

import os
import sys
import json
import shutil
import sqlite3
import logging
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional, Tuple

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('augment_cleaner.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class AugmentCleaner:
    """Augment 扩展存储清理器"""
    
    def __init__(self):
        self.vscode_data_dir = self._get_vscode_data_dir()
        self.backup_dir = Path("augment_backup") / datetime.now().strftime("%Y%m%d_%H%M%S")
        self.extension_id = "Augment.vscode-augment"
        
        # 存储路径定义
        self.storage_paths = {
            'global_storage': self.vscode_data_dir / "User" / "globalStorage" / self.extension_id,
            'workspace_storage_root': self.vscode_data_dir / "User" / "workspaceStorage",
            'user_settings': self.vscode_data_dir / "User" / "settings.json",
            'user_keybindings': self.vscode_data_dir / "User" / "keybindings.json",
            'extensions_dir': self.vscode_data_dir / "extensions",
            'logs_dir': self.vscode_data_dir / "logs",
            'cache_dir': self.vscode_data_dir / "CachedExtensions"
        }
        
        # Augment 相关的存储键值
        self.augment_keys = [
            "sidecar.Augment.vscode-augment",
            "hasEverUsedAgent",
            "userTier",
            "apiToken",
            "sessionId",
            "trialStartDate",
            "lastUsedDate",
            "featureFlags",
            "authToken",
            "refreshToken"
        ]
        
        # Augment 相关的配置键
        self.augment_config_keys = [
            "augment.advanced.apiToken",
            "augment.enableEmptyFileHint",
            "augment.conflictingCodingAssistantCheck",
            "augment.advanced.completionURL",
            "augment.advanced.integrations"
        ]
    
    def _get_vscode_data_dir(self) -> Path:
        """获取 VSCode 数据目录"""
        if sys.platform == "win32":
            return Path(os.environ.get("APPDATA", "")) / "Code"
        elif sys.platform == "darwin":
            return Path.home() / "Library" / "Application Support" / "Code"
        else:  # Linux
            return Path.home() / ".config" / "Code"
    
    def create_backup(self) -> bool:
        """创建备份"""
        try:
            logger.info(f"创建备份到: {self.backup_dir}")
            self.backup_dir.mkdir(parents=True, exist_ok=True)
            
            # 备份全局存储
            global_storage = self.storage_paths['global_storage']
            if global_storage.exists():
                backup_global = self.backup_dir / "globalStorage"
                shutil.copytree(global_storage, backup_global)
                logger.info(f"已备份全局存储: {backup_global}")
            
            # 备份工作区存储中的 Augment 数据
            workspace_root = self.storage_paths['workspace_storage_root']
            if workspace_root.exists():
                backup_workspace = self.backup_dir / "workspaceStorage"
                backup_workspace.mkdir(exist_ok=True)
                
                for workspace_dir in workspace_root.iterdir():
                    if workspace_dir.is_dir():
                        augment_workspace = workspace_dir / self.extension_id
                        if augment_workspace.exists():
                            backup_path = backup_workspace / workspace_dir.name / self.extension_id
                            backup_path.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copytree(augment_workspace, backup_path)
                            logger.info(f"已备份工作区存储: {backup_path}")
            
            # 备份用户配置
            settings_file = self.storage_paths['user_settings']
            if settings_file.exists():
                backup_settings = self.backup_dir / "settings.json"
                shutil.copy2(settings_file, backup_settings)
                logger.info(f"已备份用户配置: {backup_settings}")
            
            return True
            
        except Exception as e:
            logger.error(f"备份失败: {e}")
            return False
    
    def clean_global_storage(self) -> bool:
        """清理全局存储"""
        try:
            global_storage = self.storage_paths['global_storage']
            if global_storage.exists():
                logger.info(f"清理全局存储: {global_storage}")
                shutil.rmtree(global_storage)
                logger.info("全局存储清理完成")
                return True
            else:
                logger.info("全局存储目录不存在，跳过清理")
                return True
                
        except Exception as e:
            logger.error(f"清理全局存储失败: {e}")
            return False
    
    def clean_workspace_storage(self) -> bool:
        """清理工作区存储"""
        try:
            workspace_root = self.storage_paths['workspace_storage_root']
            if not workspace_root.exists():
                logger.info("工作区存储目录不存在，跳过清理")
                return True
            
            cleaned_count = 0
            for workspace_dir in workspace_root.iterdir():
                if workspace_dir.is_dir():
                    augment_workspace = workspace_dir / self.extension_id
                    if augment_workspace.exists():
                        logger.info(f"清理工作区存储: {augment_workspace}")
                        shutil.rmtree(augment_workspace)
                        cleaned_count += 1
            
            logger.info(f"工作区存储清理完成，共清理 {cleaned_count} 个工作区")
            return True
            
        except Exception as e:
            logger.error(f"清理工作区存储失败: {e}")
            return False
    
    def clean_user_settings(self) -> bool:
        """清理用户配置中的 Augment 相关设置"""
        try:
            settings_file = self.storage_paths['user_settings']
            if not settings_file.exists():
                logger.info("用户配置文件不存在，跳过清理")
                return True
            
            # 读取配置文件
            with open(settings_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
            
            # 移除 Augment 相关配置
            removed_keys = []
            for key in list(settings.keys()):
                if any(augment_key in key for augment_key in self.augment_config_keys):
                    del settings[key]
                    removed_keys.append(key)
            
            if removed_keys:
                # 写回配置文件
                with open(settings_file, 'w', encoding='utf-8') as f:
                    json.dump(settings, f, indent=2, ensure_ascii=False)
                
                logger.info(f"用户配置清理完成，移除了 {len(removed_keys)} 个配置项: {removed_keys}")
            else:
                logger.info("用户配置中未找到 Augment 相关配置")
            
            return True
            
        except Exception as e:
            logger.error(f"清理用户配置失败: {e}")
            return False
    
    def clean_extension_logs(self) -> bool:
        """清理扩展日志"""
        try:
            logs_dir = self.storage_paths['logs_dir']
            if not logs_dir.exists():
                logger.info("日志目录不存在，跳过清理")
                return True
            
            cleaned_count = 0
            for log_file in logs_dir.rglob("*augment*"):
                if log_file.is_file():
                    logger.info(f"清理日志文件: {log_file}")
                    log_file.unlink()
                    cleaned_count += 1
            
            logger.info(f"扩展日志清理完成，共清理 {cleaned_count} 个日志文件")
            return True
            
        except Exception as e:
            logger.error(f"清理扩展日志失败: {e}")
            return False
    
    def clean_extension_cache(self) -> bool:
        """清理扩展缓存"""
        try:
            cache_dir = self.storage_paths['cache_dir']
            if not cache_dir.exists():
                logger.info("缓存目录不存在，跳过清理")
                return True
            
            cleaned_count = 0
            for cache_file in cache_dir.rglob("*augment*"):
                if cache_file.is_file():
                    logger.info(f"清理缓存文件: {cache_file}")
                    cache_file.unlink()
                    cleaned_count += 1
                elif cache_file.is_dir():
                    logger.info(f"清理缓存目录: {cache_file}")
                    shutil.rmtree(cache_file)
                    cleaned_count += 1
            
            logger.info(f"扩展缓存清理完成，共清理 {cleaned_count} 个缓存项")
            return True
            
        except Exception as e:
            logger.error(f"清理扩展缓存失败: {e}")
            return False

    def clean_sqlite_storage(self) -> bool:
        """清理 SQLite 存储中的 Augment 数据"""
        try:
            # VSCode 可能使用 SQLite 存储一些扩展数据
            storage_db = self.vscode_data_dir / "User" / "storage.db"
            if not storage_db.exists():
                logger.info("SQLite 存储文件不存在，跳过清理")
                return True

            # 连接数据库
            conn = sqlite3.connect(storage_db)
            cursor = conn.cursor()

            # 查找 Augment 相关的表和数据
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()

            cleaned_count = 0
            for table in tables:
                table_name = table[0]
                if 'augment' in table_name.lower():
                    logger.info(f"清理表: {table_name}")
                    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
                    cleaned_count += 1

            # 清理可能包含 Augment 数据的通用表
            try:
                cursor.execute("DELETE FROM ItemTable WHERE key LIKE '%augment%'")
                deleted_rows = cursor.rowcount
                if deleted_rows > 0:
                    logger.info(f"从 ItemTable 删除了 {deleted_rows} 行 Augment 数据")
                    cleaned_count += deleted_rows
            except sqlite3.OperationalError:
                pass  # 表可能不存在

            conn.commit()
            conn.close()

            logger.info(f"SQLite 存储清理完成，共清理 {cleaned_count} 项")
            return True

        except Exception as e:
            logger.error(f"清理 SQLite 存储失败: {e}")
            return False

    def clean_registry_entries(self) -> bool:
        """清理 Windows 注册表中的 Augment 相关项（仅 Windows）"""
        if sys.platform != "win32":
            logger.info("非 Windows 系统，跳过注册表清理")
            return True

        try:
            import winreg

            # VSCode 扩展可能在注册表中存储一些信息
            registry_paths = [
                r"SOFTWARE\Microsoft\VSCode\Extensions",
                r"SOFTWARE\Classes\VSCode",
                r"HKEY_CURRENT_USER\SOFTWARE\Microsoft\VSCode"
            ]

            cleaned_count = 0
            for reg_path in registry_paths:
                try:
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_ALL_ACCESS)

                    # 枚举子键，查找 Augment 相关项
                    i = 0
                    while True:
                        try:
                            subkey_name = winreg.EnumKey(key, i)
                            if 'augment' in subkey_name.lower():
                                logger.info(f"清理注册表项: {reg_path}\\{subkey_name}")
                                winreg.DeleteKey(key, subkey_name)
                                cleaned_count += 1
                            else:
                                i += 1
                        except WindowsError:
                            break

                    winreg.CloseKey(key)

                except FileNotFoundError:
                    continue  # 注册表路径不存在
                except Exception as e:
                    logger.warning(f"清理注册表路径 {reg_path} 时出错: {e}")

            logger.info(f"注册表清理完成，共清理 {cleaned_count} 项")
            return True

        except ImportError:
            logger.warning("无法导入 winreg 模块，跳过注册表清理")
            return True
        except Exception as e:
            logger.error(f"清理注册表失败: {e}")
            return False

    def scan_augment_data(self) -> Dict[str, List[str]]:
        """扫描所有 Augment 相关数据"""
        logger.info("开始扫描 Augment 相关数据...")

        found_data = {
            'global_storage': [],
            'workspace_storage': [],
            'user_settings': [],
            'logs': [],
            'cache': [],
            'sqlite': [],
            'registry': []
        }

        # 扫描全局存储
        global_storage = self.storage_paths['global_storage']
        if global_storage.exists():
            for item in global_storage.rglob("*"):
                found_data['global_storage'].append(str(item))

        # 扫描工作区存储
        workspace_root = self.storage_paths['workspace_storage_root']
        if workspace_root.exists():
            for workspace_dir in workspace_root.iterdir():
                if workspace_dir.is_dir():
                    augment_workspace = workspace_dir / self.extension_id
                    if augment_workspace.exists():
                        for item in augment_workspace.rglob("*"):
                            found_data['workspace_storage'].append(str(item))

        # 扫描用户配置
        settings_file = self.storage_paths['user_settings']
        if settings_file.exists():
            try:
                with open(settings_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)

                for key in settings.keys():
                    if any(augment_key in key for augment_key in self.augment_config_keys):
                        found_data['user_settings'].append(f"{key}: {settings[key]}")
            except Exception as e:
                logger.warning(f"扫描用户配置时出错: {e}")

        # 扫描日志
        logs_dir = self.storage_paths['logs_dir']
        if logs_dir.exists():
            for log_file in logs_dir.rglob("*augment*"):
                found_data['logs'].append(str(log_file))

        # 扫描缓存
        cache_dir = self.storage_paths['cache_dir']
        if cache_dir.exists():
            for cache_item in cache_dir.rglob("*augment*"):
                found_data['cache'].append(str(cache_item))

        return found_data

    def print_scan_results(self, found_data: Dict[str, List[str]]):
        """打印扫描结果"""
        logger.info("=== Augment 数据扫描结果 ===")

        total_items = 0
        for category, items in found_data.items():
            if items:
                logger.info(f"\n{category.upper()} ({len(items)} 项):")
                for item in items[:10]:  # 只显示前10项
                    logger.info(f"  - {item}")
                if len(items) > 10:
                    logger.info(f"  ... 还有 {len(items) - 10} 项")
                total_items += len(items)
            else:
                logger.info(f"\n{category.upper()}: 未找到相关数据")

        logger.info(f"\n总计找到 {total_items} 项 Augment 相关数据")

    def full_clean(self, create_backup: bool = True) -> bool:
        """执行完整清理"""
        logger.info("开始执行 Augment 扩展完整清理...")

        # 创建备份
        if create_backup:
            if not self.create_backup():
                logger.error("备份失败，终止清理操作")
                return False

        # 执行各项清理
        success = True

        success &= self.clean_global_storage()
        success &= self.clean_workspace_storage()
        success &= self.clean_user_settings()
        success &= self.clean_extension_logs()
        success &= self.clean_extension_cache()
        success &= self.clean_sqlite_storage()
        success &= self.clean_registry_entries()

        if success:
            logger.info("✅ Augment 扩展完整清理成功完成！")
        else:
            logger.error("❌ 清理过程中出现错误，请检查日志")

        return success

    def restore_from_backup(self, backup_path: str) -> bool:
        """从备份恢复"""
        try:
            backup_dir = Path(backup_path)
            if not backup_dir.exists():
                logger.error(f"备份目录不存在: {backup_dir}")
                return False

            logger.info(f"从备份恢复: {backup_dir}")

            # 恢复全局存储
            backup_global = backup_dir / "globalStorage"
            if backup_global.exists():
                target_global = self.storage_paths['global_storage']
                if target_global.exists():
                    shutil.rmtree(target_global)
                shutil.copytree(backup_global, target_global)
                logger.info("已恢复全局存储")

            # 恢复工作区存储
            backup_workspace = backup_dir / "workspaceStorage"
            if backup_workspace.exists():
                workspace_root = self.storage_paths['workspace_storage_root']
                for workspace_backup in backup_workspace.iterdir():
                    if workspace_backup.is_dir():
                        target_workspace = workspace_root / workspace_backup.name / self.extension_id
                        if target_workspace.exists():
                            shutil.rmtree(target_workspace)
                        target_workspace.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copytree(workspace_backup / self.extension_id, target_workspace)
                        logger.info(f"已恢复工作区存储: {workspace_backup.name}")

            # 恢复用户配置
            backup_settings = backup_dir / "settings.json"
            if backup_settings.exists():
                target_settings = self.storage_paths['user_settings']
                shutil.copy2(backup_settings, target_settings)
                logger.info("已恢复用户配置")

            logger.info("✅ 从备份恢复成功完成！")
            return True

        except Exception as e:
            logger.error(f"从备份恢复失败: {e}")
            return False


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="Augment VSCode 扩展本地存储完整清理工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  python augment_cleaner.py --scan                    # 扫描 Augment 数据
  python augment_cleaner.py --clean                   # 完整清理（自动备份）
  python augment_cleaner.py --clean --no-backup      # 完整清理（不备份）
  python augment_cleaner.py --restore backup_path    # 从备份恢复
  python augment_cleaner.py --clean-global           # 只清理全局存储
  python augment_cleaner.py --clean-workspace        # 只清理工作区存储
        """
    )

    parser.add_argument('--scan', action='store_true', help='扫描 Augment 相关数据')
    parser.add_argument('--clean', action='store_true', help='执行完整清理')
    parser.add_argument('--no-backup', action='store_true', help='清理时不创建备份')
    parser.add_argument('--restore', type=str, help='从指定备份路径恢复')
    parser.add_argument('--clean-global', action='store_true', help='只清理全局存储')
    parser.add_argument('--clean-workspace', action='store_true', help='只清理工作区存储')
    parser.add_argument('--clean-settings', action='store_true', help='只清理用户配置')
    parser.add_argument('--clean-logs', action='store_true', help='只清理扩展日志')
    parser.add_argument('--clean-cache', action='store_true', help='只清理扩展缓存')
    parser.add_argument('--clean-sqlite', action='store_true', help='只清理 SQLite 存储')
    parser.add_argument('--clean-registry', action='store_true', help='只清理注册表项（Windows）')

    args = parser.parse_args()

    # 检查是否有 VSCode 进程运行
    try:
        import psutil
        vscode_processes = [p for p in psutil.process_iter(['pid', 'name']) if 'code' in p.info['name'].lower()]
        if vscode_processes:
            logger.warning("检测到 VSCode 正在运行，建议先关闭 VSCode 再执行清理操作")
            response = input("是否继续？(y/N): ")
            if response.lower() != 'y':
                logger.info("操作已取消")
                return
    except ImportError:
        logger.warning("无法检测 VSCode 进程状态，建议手动确认 VSCode 已关闭")

    cleaner = AugmentCleaner()

    if args.scan:
        found_data = cleaner.scan_augment_data()
        cleaner.print_scan_results(found_data)

    elif args.clean:
        create_backup = not args.no_backup
        success = cleaner.full_clean(create_backup)
        if success:
            logger.info("清理完成！重启 VSCode 后 Augment 扩展将处于全新状态")
        else:
            logger.error("清理过程中出现错误，请检查日志文件")

    elif args.restore:
        success = cleaner.restore_from_backup(args.restore)
        if success:
            logger.info("恢复完成！重启 VSCode 后 Augment 扩展将恢复到备份状态")
        else:
            logger.error("恢复过程中出现错误，请检查日志文件")

    elif args.clean_global:
        cleaner.clean_global_storage()

    elif args.clean_workspace:
        cleaner.clean_workspace_storage()

    elif args.clean_settings:
        cleaner.clean_user_settings()

    elif args.clean_logs:
        cleaner.clean_extension_logs()

    elif args.clean_cache:
        cleaner.clean_extension_cache()

    elif args.clean_sqlite:
        cleaner.clean_sqlite_storage()

    elif args.clean_registry:
        cleaner.clean_registry_entries()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
