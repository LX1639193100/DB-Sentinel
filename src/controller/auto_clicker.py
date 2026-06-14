# -*- coding: utf-8 -*-
"""
自动点击器
"""

import pyautogui
import time
import random
from typing import Tuple
from loguru import logger


class AutoClicker:
    """自动点击器"""
    
    def __init__(self, config: dict):
        """
        初始化点击器
        
        Args:
            config: 配置字典
        """
        self.config = config
        self.controller_config = config.get('controller', {})
        
        # 启用防检测
        pyautogui.FAILSAFE = True
    
    def click(self, x: int, y: int, delay: float = None) -> bool:
        """
        点击指定位置
        
        Args:
            x: X坐标
            y: Y坐标
            delay: 点击延迟(秒)
            
        Returns:
            是否成功
        """
        try:
            # 添加随机偏移
            if self.controller_config.get('random_offset', False):
                offset_range = self.controller_config.get('offset_range', 10)
                x += random.randint(-offset_range, offset_range)
                y += random.randint(-offset_range, offset_range)
            
            # 计算点击延迟
            if delay is None:
                min_delay = self.controller_config.get('click_delay_min', 50) / 1000
                max_delay = self.controller_config.get('click_delay_max', 150) / 1000
                delay = random.uniform(min_delay, max_delay)
            
            # 执行点击
            pyautogui.click(x, y)
            logger.debug(f"Clicked at ({x}, {y})")
            
            # 等待
            time.sleep(delay)
            
            return True
        
        except Exception as e:
            logger.error(f"Click failed: {e}")
            return False
    
    def click_multiple(self, positions: list) -> int:
        """
        点击多个位置
        
        Args:
            positions: 坐标列表 [(x1, y1), (x2, y2), ...]
            
        Returns:
            成功点击的次数
        """
        success_count = 0
        for x, y in positions:
            if self.click(x, y):
                success_count += 1
        return success_count
    
    def move_mouse(self, x: int, y: int, duration: float = 0.5):
        """
        移动鼠标
        
        Args:
            x: 目标X坐标
            y: 目标Y坐标
            duration: 持续时间(秒)
        """
        try:
            speed = self.controller_config.get('mouse_speed', 0.5)
            pyautogui.moveTo(x, y, duration=duration * speed)
            logger.debug(f"Moved mouse to ({x}, {y})")
        except Exception as e:
            logger.error(f"Mouse move failed: {e}")
