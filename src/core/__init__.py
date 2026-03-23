import importlib
from pathlib import Path

# 自动发现所有.py文件（排除__init__.py）
module_files = [
    f.stem for f in Path(__file__).parent.glob("*.py") 
    if f.is_file() and f.stem != "__init__"
]

# 动态导入模块
for module_name in module_files:
    try:
        # 使用相对导入
        module = importlib.import_module(f".{module_name}", package=__package__)
        globals()[module_name] = module
    except ImportError:
        pass

__all__ = list(module_files)