#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抖音自动福袋助手 - 主程序入口
Douyin Lucky Bag Assistant - Main Entry
"""

import sys
import os
from pathlib import Path

# 添加源代码路径
sys.path.insert(0, str(Path(__file__).parent))

from PyQt5.QtWidgets import QApplication
from loguru import logger

from src.ui.main_window import MainWindow
from src.utils.constants import APP_NAME, APP_VERSION, LOG_DIR


def setup_logging():
    """配置日志系统"""
    log_file = LOG_DIR / "app_{time:YYYY-MM-DD}.log"
    
    # 移除默认处理器
    logger.remove()
    
    # 添加文件处理器
    logger.add(
        str(log_file),
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="500 MB",
        retention="7 days"
    )
    
    # 添加控制台处理器
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO"
    )


def main():
    """主函数"""
    # 创建日志目录
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    
    # 设置日志
    setup_logging()
    logger.info(f"Starting {APP_NAME} v{APP_VERSION}")
    
    # 创建应用
    app = QApplication(sys.argv)
    
    # 设置应用信息
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    
    # 创建主窗口
    window = MainWindow()
    window.show()
    
    logger.info("Main window displayed")
    
    # 运行应用
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
