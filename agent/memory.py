# Simple in-memory logging for demo
memory_log = []

def log(action: str):
    memory_log.append(action)

def get_log():
    return memory_log