# -*- coding: utf-8 -*-
"""
统计模块
"""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List
from loguru import logger


class Statistics:
    """统计器"""
    
    def __init__(self, config: dict):
        """
        初始化统计器
        
        Args:
            config: 配置字典
        """
        self.config = config
        self.logger_config = config.get('logger', {})
        self.statistics_file = Path(self.logger_config.get('statistics_file', 'data/statistics.json'))
        self.statistics_file.parent.mkdir(parents=True, exist_ok=True)
        
        self.data = self.load_statistics()
    
    def load_statistics(self) -> Dict:
        """
        加载统计数据
        
        Returns:
            统计数据字典
        """
        if self.statistics_file.exists():
            try:
                with open(self.statistics_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load statistics: {e}")
        
        return {
            'total_bags': 0,
            'total_money': 0.0,
            'records': []
        }
    
    def save_statistics(self):
        """
        保存统计数据
        """
        try:
            with open(self.statistics_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            logger.debug(f"Statistics saved to {self.statistics_file}")
        except Exception as e:
            logger.error(f"Failed to save statistics: {e}")
    
    def record_lucky_bag(self, amount: float = 0.0, status: str = "success"):
        """
        记录福袋
        
        Args:
            amount: 红包金额
            status: 状态 (success, failed, etc.)
        """
        record = {
            'timestamp': datetime.now().isoformat(),
            'amount': amount,
            'status': status
        }
        
        self.data['records'].append(record)
        self.data['total_bags'] += 1
        self.data['total_money'] += amount
        
        self.save_statistics()
        logger.info(f"Recorded lucky bag: amount={amount}, status={status}")
    
    def get_today_stats(self) -> Dict:
        """
        获取今日统计
        
        Returns:
            今日统计数据
        """
        today = datetime.now().date()
        today_records = []
        today_money = 0.0
        
        for record in self.data['records']:
            record_date = datetime.fromisoformat(record['timestamp']).date()
            if record_date == today:
                today_records.append(record)
                today_money += record['amount']
        
        return {
            'count': len(today_records),
            'total': today_money,
            'records': today_records
        }
    
    def get_summary(self) -> Dict:
        """
        获取统计摘要
        
        Returns:
            摘要信息
        """
        return {
            'total_bags': self.data['total_bags'],
            'total_money': self.data['total_money'],
            'today': self.get_today_stats()
        }
