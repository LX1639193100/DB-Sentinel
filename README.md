# 🛡️ DB-Sentinel: AI-Driven Multi-Agent Database Autonomic System

[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-green.svg)](https://www.python.org/)
[![MySQL Support](https://img.shields.io/badge/mysql-5.7%20%7C%208.0-orange.svg)](https://www.mysql.com/)

**DB-Sentinel** 是一款突破传统运维模式的“自愈型”数据库压测与诊断平台。它通过多智能体协同（Multi-Agent Collaboration），实现了从性能压测到根因分析、再到自动化优化的全链路闭环。

---

## ✨ 核心特性

- **🚀 工业级压测引擎**: 基于异步 IO 与连接池技术，支持模拟数千级并发用户，精准探测吞吐量（TPS）与延迟曲线。
- **🧠 多智能体协同诊断**: 
  - **Diagnostic-Agent**: 利用逻辑推理链（CoT）实时解析全表扫描、死锁锁簇等异常。
  - **Optimization-Agent**: 自动生成符合 SQL 规范的优化建议，并预测优化后的性能提升。
- **📈 实时指标洞察**: 自动抓取 InnoDB 缓冲池命中率、磁盘 I/O 等底层指标。
- **🤖 交互式 AI 报告**: 压测结束后，自动生成一份具有深度业务洞察的 PDF 报告。

## 🏗️ 系统架构
```mermaid
graph TD
    A[用户指令] --> B{Commander Agent}
    B --> C[Stress Engine]
    B --> D[Monitoring Agent]
    C --> E[(MySQL Target)]
    D --> E
    E --> F[Log/Metrics Collector]
    F --> G[Reasoning Agent]
    G --> H[AI Diagnostic Report]
