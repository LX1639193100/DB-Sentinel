from openai import OpenAI


class DiagnosticAgent:
    def __init__(self, config):
        self.client = OpenAI(api_key=config['api_key'], base_url=config.get('base_url'))

    def analyze(self, stats, slow_logs):
        prompt = f"""
        你是一位高级 DBA。当前数据库在高并发压测下表现如下：
        - TPS: {stats['tps']}
        - 平均响应时间: {stats['avg_latency']}ms
        - 错误率: {stats['error_rate']}%

        采集到的慢查询示例: {slow_logs}

        请进行根因分析并给出具体的 SQL 优化建议。要求输出精炼、专业。
        """
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": "You are a database performance expert."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content