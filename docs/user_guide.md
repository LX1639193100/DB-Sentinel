# 抖音自动福袋助手 - 用户指南

## 目录

1. [快速开始](#快速开始)
2. [基础使用](#基础使用)
3. [高级配置](#高级配置)
4. [常见问题](#常见问题)
5. [故障排除](#故障排除)

## 快速开始

### 安装

1. 克隆仓库
```bash
git clone https://github.com/LX1639193100/DB-Sentinel.git
cd DB-Sentinel
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行应用
```bash
python main.py
```

## 基础使用

### 启动监测

1. 打开应用
2. 在"监测"标签页中点击"开始监测"
3. 应用将自动监测福袋
4. 检测到福袋后会自动点击领取

### 查看统计

切换到"统计"标签页查看领取历史和金额统计。

## 高级配置

编辑 `config.yaml` 文件进行高级配置：

### 检测参数

```yaml
detector:
  # 福袋颜色范围 (HSV)
  luckybag_color_lower: [100, 50, 0]
  luckybag_color_upper: [179, 255, 255]
  
  # 最小检测面积
  min_area: 500
  
  # 检测间隔(秒)
  detection_interval: 0.1
```

### 控制参数

```yaml
controller:
  # 点击延迟范围(毫秒)
  click_delay_min: 50
  click_delay_max: 150
  
  # 启用随机偏移
  random_offset: true
  offset_range: 10
```

## 常见问题

### Q: 应用无法检测到福袋？

**A:** 检查以下项：
- 直播间是否正在进行中
- 屏幕分辨率是否满足最小要求(1920x1080)
- 福袋颜色设置是否正确

### Q: 识别准确率很低？

**A:** 调整以下参数：
- 增加 `min_area` 值
- 调整 `luckybag_color_lower` 和 `luckybag_color_upper`
- 改变检测灵敏度

## 故障排除

### 应用崩溃

1. 检查 Python 版本是否为 3.8+
2. 重新安装依赖: `pip install -r requirements.txt --upgrade`
3. 查看日志文件: `logs/lucky_bag.log`

### 无法点击福袋

1. 确保应用窗口有焦点
2. 检查是否有防火墙阻止
3. 尝试禁用其他自动化工具
