import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")

def read_file(filename: str) -> str:
    """Read file content from data directory."""
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"File {filename} not found."

def list_files():
    return os.listdir(DATA_DIR)