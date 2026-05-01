import asyncio
import aiomysql
import time


class AsyncStressEngine:
    def __init__(self, db_config):
        self.db_config = db_config
        self.metrics = {"success": 0, "failure": 0, "latencies": []}

    async def worker(self, pool):
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                start = time.perf_counter()
                try:
                    await cur.execute("SELECT * FROM users ORDER BY RAND() LIMIT 1")
                    await cur.fetchone()
                    self.metrics["latencies"].append(time.perf_counter() - start)
                    self.metrics["success"] += 1
                except Exception as e:
                    self.metrics["failure"] += 1

    async def run(self, concurrency, duration):
        pool = await aiomysql.create_pool(
            **self.db_config, minsize=10, maxsize=concurrency
        )
        print(f"[Engine] 并发级别 {concurrency} 启动...")
        end_time = time.time() + duration

        while time.time() < end_time:
            tasks = [self.worker(pool) for _ in range(concurrency)]
            await asyncio.gather(*tasks)
            await asyncio.sleep(0.05)  # 控制发压频率

        pool.close()
        await pool.wait_closed()
        return self.metrics