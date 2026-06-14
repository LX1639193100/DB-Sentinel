# -*- coding: utf-8 -*-
"""
抖音福袋监测器
"""

import cv2
import numpy as np
from typing import Optional, Dict, List
from loguru import logger
import pyautogui
import time


class DouyinMonitor:
    """抖音福袋监测器"""
    
    def __init__(self, config: dict):
        """
        初始化监测器
        
        Args:
            config: 配置字典
        """
        self.config = config
        self.detector_config = config.get('detector', {})
        self.last_detection_time = 0
    
    def detect(self) -> Optional[Dict]:
        """
        检测福袋
        
        Returns:
            检测结果字典或None
        """
        try:
            # 截屏
            screenshot = pyautogui.screenshot()
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            
            # 转换为HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            # 获取颜色范围
            lower = np.array(self.detector_config.get('luckybag_color_lower', [100, 50, 0]))
            upper = np.array(self.detector_config.get('luckybag_color_upper', [179, 255, 255]))
            
            # 创建掩码
            mask = cv2.inRange(hsv, lower, upper)
            
            # 寻找轮廓
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            
            # 过滤有效的福袋
            min_area = self.detector_config.get('min_area', 500)
            valid_bags = []
            
            for contour in contours:
                area = cv2.contourArea(contour)
                if area >= min_area:
                    x, y, w, h = cv2.boundingRect(contour)
                    valid_bags.append({
                        'x': x,
                        'y': y,
                        'width': w,
                        'height': h,
                        'area': area,
                        'confidence': area / (frame.shape[0] * frame.shape[1])
                    })
            
            if valid_bags:
                logger.debug(f"Detected {len(valid_bags)} lucky bags")
                return {
                    'count': len(valid_bags),
                    'bags': valid_bags,
                    'timestamp': time.time()
                }
            
            return None
        
        except Exception as e:
            logger.error(f"Detection failed: {e}")
            return None
    
    def get_detection_interval(self) -> float:
        """
        获取检测间隔
        
        Returns:
            间隔时间(秒)
        """
        return self.detector_config.get('detection_interval', 0.1)
