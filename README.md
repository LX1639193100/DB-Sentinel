# 抖音自动福袋助手 (Douyin Lucky Bag Assistant)

一个功能强大的PC端抖音自动福袋领取助手，支持自动监测、快速领取、数据统计等功能。

## 功能特性

- 🎯 **自动监测福袋**: 实时监测抖音直播间福袋弹幕信息
- ⚡ **秒速领取**: 智能识别并自动点击福袋领取按钮
- 📊 **数据统计**: 记录领取历史、获得红包金额统计
- 🎨 **友好UI**: 现代化图形界面，操作简单直观
- 🔧 **可配置**: 灵活的配置系统，支持自定义参数
- 🛡️ **安全稳定**: 采用图像识别和OCR技术，稳定可靠

## 系统要求

- Windows 10/11 或 macOS 10.15+
- Python 3.8+
- 最小分辨率: 1920x1080

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行应用

```bash
python main.py
```

### 3. 配置参数

编辑 `config.yaml` 文件配置识别参数和领取策略

## 项目结构

```
.
├── main.py                 # 主程序入口
├── requirements.txt        # 依赖列表
├── config.yaml            # 配置文件
├── src/
│   ├── __init__.py
│   ├── ui/                # 用户界面模块
│   │   ├── main_window.py
│   │   ├── settings_dialog.py
│   │   └── utils.py
│   ├── detector/          # 福袋检测模块
│   │   ├── douyin_monitor.py
│   │   ├── image_processor.py
│   │   └── ocr_engine.py
│   ├── controller/        # 自动控制模块
│   │   ├── auto_clicker.py
│   │   └── keyboard_handler.py
│   ├── logger/            # 日志统计模块
│   │   ├── statistics.py
│   │   └── data_persistence.py
│   └── utils/             # 工具函数
│       ├── constants.py
│       └── helpers.py
├── tests/                 # 测试模块
│   ├── test_detector.py
│   └── test_controller.py
├── docs/                  # 文档
│   └── user_guide.md
└── assets/               # 资源文件
    └── icons/
```

## 使用说明

### 基础使用

1. 启动应用后，点击"开始监测"按钮
2. 选择目标直播间
3. 应用将自动监测福袋并快速领取
4. 在统计面板查看收益数据

### 高级配置

详见 [用户指南](docs/user_guide.md)

## 注意事项

⚠️ **重要**：
- 本工具仅供学习研究使用
- 使用过程中需遵守抖音平台的用户协议
- 不建议24小时不间断运行
- 建议在娱乐场景下适度使用

## 开发指南

### 本地开发环境搭建

```bash
git clone https://github.com/LX1639193100/douyin-luckyba-assistant.git
cd douyin-luckyba-assistant
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 运行测试

```bash
pytest tests/
```

## 常见问题

### Q: 应用无法检测到福袋？
A: 请检查：
   1. 直播间是否正在进行中
   2. 是否有福袋弹幕出现
   3. 屏幕分辨率是否满足最小要求

### Q: 如何提高识别准确率？
A: 在配置文件中调整以下参数：
   - `ocr_confidence_threshold`: 提高识别阈值
   - `color_threshold`: 调整颜色识别范围

## 贡献指南

欢迎提交Issue和Pull Request！

## 许可证

MIT License

## 声明

本项目仅供学习和研究使用，使用者需自行承担使用本工具产生的一切后果。
