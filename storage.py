import os

DATA_FILE = "data.txt"
LOG_FILE = "logs.txt"

def save_to_file(message, result):
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{message} | {result}\n")

def load_data():
    data = []

    if not os.path.exists(DATA_FILE):
        return data

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(" | ")
            if len(parts) == 2:
                data.append((parts[0], parts[1]))

    return data

def log_action(action):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(action + "\n")


def clear_data():
    open(DATA_FILE, "w").close()
    log_action("DATA CLEARED")