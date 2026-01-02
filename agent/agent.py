from agent.planner import plan_task
from agent.tools import read_file
from agent.memory import log

class Agent:
    def __init__(self):
        self.reasoning = []

    def run(self, task: str):
        steps = plan_task(task)
        self.reasoning.extend(steps)
        log(f"Planned steps for task: {task}")

        # Execute steps (demo purposes)
        sales = read_file("sales.csv")
        payroll = read_file("payroll.csv")
        legal = read_file("legal_memo.txt")

        summary = f"Sales summary: {sales.strip()}\nPayroll info: {payroll.strip()}"

        self.reasoning.append("Executed reading sales.csv, payroll.csv, legal_memo.txt")
        log("Executed file reads")

        return {
            "summary": summary,
            "reasoning": self.reasoning
        }