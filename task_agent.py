import json
import os

TASK_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []


tasks = load_tasks()


def save_tasks():
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks.append(task)
    save_tasks()


def get_tasks():
    return tasks