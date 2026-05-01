import asyncio
import yaml
import sys
from core.engine import AsyncStressEngine
from agents.diagnostic_agent import DiagnosticAgent


async def start_pipeline():
    # 1. 加载配置
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # 2. 执行异步压测
    engine = AsyncStressEngine(config['db'])
    start_t = time.time()
    raw_data = await engine.run(config['stress']['concurrency'], config['stress']['duration'])
    duration = time.time() - start_t

    # 3. 计算指标
    tps = raw_data['success'] / duration
    avg_latency = (sum(raw_data['latencies']) / len(raw_data['latencies'])) * 1000 if raw_data['latencies'] else 0
    stats = {
        "tps": round(tps, 2),
        "avg_latency": round(avg_latency, 2),
        "error_rate": round((raw_data['failure'] / (raw_data['success'] + raw_data['failure'])) * 100, 2)
    }

    print(f"\n📊 压测报告: TPS={stats['tps']}, Latency={stats['avg_latency']}ms")

    # 4. AI 诊断
    print("🤖 多代理协同诊断中...")
    agent = DiagnosticAgent(config['ai'])
    report = agent.analyze(stats, "SELECT * FROM users WHERE email LIKE '%user%';")

    print("\n" + "=" * 50)
    print("📜 AI 自治诊断报告")
    print("=" * 50)
    print(report)


if __name__ == "__main__":
    import time

    asyncio.run(start_pipeline())