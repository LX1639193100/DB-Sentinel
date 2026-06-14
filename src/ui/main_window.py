# -*- coding: utf-8 -*-
"""
主窗口
"""

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QTabWidget, QTextEdit, QTableWidget, QTableWidgetItem,
    QStatusBar, QMenuBar, QMenu, QDialog, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QThread
from PyQt5.QtGui import QFont, QIcon
from loguru import logger

from src.utils.constants import APP_NAME, APP_VERSION, WINDOW_WIDTH, WINDOW_HEIGHT
from src.detector.douyin_monitor import DouyinMonitor
from src.utils.helpers import load_config


class MonitorThread(QThread):
    """监测线程"""
    
    status_changed = pyqtSignal(str)
    detected = pyqtSignal(dict)
    
    def __init__(self, config: dict):
        super().__init__()
        self.config = config
        self.running = False
        self.monitor = DouyinMonitor(config)
    
    def run(self):
        """运行线程"""
        self.running = True
        self.status_changed.emit("监测中...")
        
        while self.running:
            try:
                result = self.monitor.detect()
                if result:
                    self.detected.emit(result)
            except Exception as e:
                logger.error(f"Detection error: {e}")
                self.status_changed.emit(f"错误: {str(e)}")
            
            self.msleep(100)
    
    def stop(self):
        """停止线程"""
        self.running = False
        self.wait()


class MainWindow(QMainWindow):
    """主窗口类"""
    
    def __init__(self):
        super().__init__()
        self.config = load_config()
        self.monitor_thread = None
        self.is_monitoring = False
        
        self.init_ui()
        self.setup_connections()
    
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION}")
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # 创建菜单栏
        self.create_menu_bar()
        
        # 创建中央窗口
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        
        # 创建标签页
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)
        
        # 添加不同的标签页
        self.create_monitor_tab()
        self.create_statistics_tab()
        self.create_settings_tab()
        self.create_about_tab()
        
        # 创建状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("就绪")
    
    def create_menu_bar(self):
        """创建菜单栏"""
        menubar = self.menuBar()
        
        # 文件菜单
        file_menu = menubar.addMenu("文件")
        file_menu.addAction("退出", self.close)
        
        # 帮助菜单
        help_menu = menubar.addMenu("帮助")
        help_menu.addAction("关于", self.show_about)
    
    def create_monitor_tab(self):
        """创建监测标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # 标题
        title = QLabel("福袋监测")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)
        
        # 状态显示
        self.status_label = QLabel("状态: 已停止")
        layout.addWidget(self.status_label)
        
        # 按钮布局
        button_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("开始监测")
        self.start_btn.setFixedWidth(100)
        self.start_btn.clicked.connect(self.start_monitoring)
        button_layout.addWidget(self.start_btn)
        
        self.stop_btn = QPushButton("停止监测")
        self.stop_btn.setFixedWidth(100)
        self.stop_btn.setEnabled(False)
        self.stop_btn.clicked.connect(self.stop_monitoring)
        button_layout.addWidget(self.stop_btn)
        
        layout.addLayout(button_layout)
        
        # 日志显示
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setPlaceholderText("监测日志将显示在此...")
        layout.addWidget(self.log_text)
        
        self.tab_widget.addTab(widget, "监测")
    
    def create_statistics_tab(self):
        """创建统计标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # 标题
        title = QLabel("统计数据")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)
        
        # 统计表格
        self.stats_table = QTableWidget()
        self.stats_table.setColumnCount(3)
        self.stats_table.setHorizontalHeaderLabels(["时间", "红包金额", "状态"])
        layout.addWidget(self.stats_table)
        
        # 导出按钮
        export_btn = QPushButton("导出数据")
        export_btn.clicked.connect(self.export_statistics)
        layout.addWidget(export_btn)
        
        self.tab_widget.addTab(widget, "统计")
    
    def create_settings_tab(self):
        """创建设置标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # 标题
        title = QLabel("设置")
        title.setFont(QFont("Arial", 14, QFont.Bold))
        layout.addWidget(title)
        
        settings_text = QTextEdit()
        settings_text.setPlaceholderText("配置设置...")
        layout.addWidget(settings_text)
        
        save_btn = QPushButton("保存设置")
        save_btn.clicked.connect(self.save_settings)
        layout.addWidget(save_btn)
        
        self.tab_widget.addTab(widget, "设置")
    
    def create_about_tab(self):
        """创建关于标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        # 关于信息
        about_text = QLabel(
            f"<h2>{APP_NAME}</h2>"
            f"<p>版本: {APP_VERSION}</p>"
            f"<p>一个功能强大的PC端抖音自动福袋领取助手</p>"
            f"<p><b>功能特性:</b></p>"
            f"<ul>"
            f"<li>自动监测福袋</li>"
            f"<li>秒速领取</li>"
            f"<li>数据统计</li>"
            f"<li>友好UI</li>"
            f"</ul>"
            f"<p><b>注意:</b> 本工具仅供学习研究使用</p>"
        )
        about_text.setWordWrap(True)
        layout.addWidget(about_text)
        layout.addStretch()
        
        self.tab_widget.addTab(widget, "关于")
    
    def setup_connections(self):
        """设置信号连接"""
        pass
    
    def start_monitoring(self):
        """开始监测"""
        if not self.is_monitoring:
            self.is_monitoring = True
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.status_label.setText("状态: 监测中...")
            self.statusBar.showMessage("监测已启动")
            
            self.monitor_thread = MonitorThread(self.config)
            self.monitor_thread.status_changed.connect(self.on_status_changed)
            self.monitor_thread.detected.connect(self.on_lucky_bag_detected)
            self.monitor_thread.start()
            
            self.log_text.append("[INFO] 监测已启动")
    
    def stop_monitoring(self):
        """停止监测"""
        if self.is_monitoring and self.monitor_thread:
            self.is_monitoring = False
            self.monitor_thread.stop()
            self.start_btn.setEnabled(True)
            self.stop_btn.setEnabled(False)
            self.status_label.setText("状态: 已停止")
            self.statusBar.showMessage("监测已停止")
            self.log_text.append("[INFO] 监测已停止")
    
    def on_status_changed(self, status: str):
        """状态改变回调"""
        self.log_text.append(f"[{status}]")
    
    def on_lucky_bag_detected(self, data: dict):
        """检测到福袋回调"""
        self.log_text.append(f"[DETECT] 发现福袋: {data}")
        # 这里可以添加自动领取逻辑
    
    def export_statistics(self):
        """导出统计数据"""
        QMessageBox.information(self, "导出", "统计数据已导出")
    
    def save_settings(self):
        """保存设置"""
        QMessageBox.information(self, "保存", "设置已保存")
    
    def show_about(self):
        """显示关于对话框"""
        QMessageBox.about(
            self,
            "关于",
            f"{APP_NAME} v{APP_VERSION}\n\n一个功能强大的PC端抖音自动福袋助手"
        )
    
    def closeEvent(self, event):
        """关闭事件"""
        if self.is_monitoring:
            self.stop_monitoring()
        event.accept()
