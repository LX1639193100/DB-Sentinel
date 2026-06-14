# -*- coding: utf-8 -*-
"""
常量定义
"""

from pathlib import Path

# 应用信息
APP_NAME = "抖音自动福袋助手"
APP_VERSION = "1.0.0"
APP_AUTHOR = "LX1639193100"

# 路径配置
BASE_DIR = Path(__file__).parent.parent.parent
SRC_DIR = BASE_DIR / "src"
LOG_DIR = BASE_DIR / "logs"
DATA_DIR = BASE_DIR / "data"
CONFIG_DIR = BASE_DIR / "config"
ASSET_DIR = BASE_DIR / "assets"

# 确保目录存在
for directory in [LOG_DIR, DATA_DIR, CONFIG_DIR, ASSET_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# 颜色定义 (RGB)
COLOR_PRIMARY = (0, 122, 204)
COLOR_SUCCESS = (34, 177, 76)
COLOR_WARNING = (255, 193, 7)
COLOR_DANGER = (229, 57, 53)
COLOR_INFO = (33, 150, 243)

# 福袋相关常量
LUCKY_BAG_DETECT_INTERVAL = 0.1  # 秒
LUCKY_BAG_CLICK_DELAY = 0.05     # 秒
LUCKY_BAG_COOLDOWN = 1            # 秒

# 屏幕相关
MIN_SCREEN_WIDTH = 1920
MIN_SCREEN_HEIGHT = 1080

# UI相关
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
