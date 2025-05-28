import os
import json
import shutil
import platform

def get_vscode_settings_path():
    system = platform.system()
    if system == "Windows":
        return os.path.expandvars(r"%APPDATA%\Code\User\settings.json")
    elif system == "Darwin":
        return os.path.expanduser("~/Library/Application Support/Code/User/settings.json")
    else:
        return os.path.expanduser("~/.config/Code/User/settings.json")

def get_extensions_dir():
    system = platform.system()
    if system == "Windows":
        return os.path.expandvars(r"%USERPROFILE%\.vscode\extensions")
    else:
        return os.path.expanduser("~/.vscode/extensions")

def clear_api_token(settings_path):
    print(f"检查 VS Code 设置文件: {settings_path}")
    if not os.path.exists(settings_path):
        print(f"未找到 VS Code 设置文件: {settings_path}")
        return
    with open(settings_path, "r", encoding="utf-8") as f:
        try:
            settings = json.load(f)
        except Exception:
            print("settings.json 解析失败，跳过 API Token 清理。")
            return
    if "augment.advanced.apiToken" in settings:
        del settings["augment.advanced.apiToken"]
        with open(settings_path, "w", encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=2)
        print("已清空 API Token")
    else:
        print("未找到 API Token，无需清理。")

def clear_augment_globalstorage(extensions_dir):
    print(f"检查扩展目录: {extensions_dir}")
    if not os.path.exists(extensions_dir):
        print(f"未找到扩展目录: {extensions_dir}")
        return
    found = False
    for name in os.listdir(extensions_dir):
        if name.startswith("augment.vscode-augment"):
            global_storage = os.path.join(extensions_dir, name, "globalStorage")
            print(f"检查 {global_storage}")
            if os.path.exists(global_storage):
                shutil.rmtree(global_storage)
                print(f"已删除 {global_storage}")
                found = True
    if not found:
        print("未找到 Augment 扩展 globalStorage，无需清理。")

if __name__ == "__main__":
    settings_path = get_vscode_settings_path()
    extensions_dir = get_extensions_dir()
    print("settings_path:", settings_path)
    print("extensions_dir:", extensions_dir)
    clear_api_token(settings_path)
    clear_augment_globalstorage(extensions_dir)
    print("Augment 身份ID已全部清空，请重启 VS Code。") 