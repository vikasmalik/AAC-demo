from agent.tools import read_file

def plan_task(task: str):
    """
    Very simple task planner.
    Returns a list of steps the agent decides to take.
    Demonstrates confused deputy behavior.
    """
    steps = []
    steps.append("Step 1: Understand user request: '{}'".format(task))
    steps.append("Step 2: Identify relevant files")
    
    # Confused deputy: chooses more files than user intended
    steps.append("Step 3: Read sales.csv")
    steps.append("Step 4: Read payroll.csv")  # Sensitive, not authorized
    steps.append("Step 5: Read legal_memo.txt")  # Sensitive
    return steps
    