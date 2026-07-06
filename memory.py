import json
import os

MEMORY_FILE = "memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}


memory = load_memory()


def save_memory(key, value):
    memory[key] = value

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def get_memory(key):
    return memory.get(key)


def get_all_memory():
    return memory


def delete_memory(key):
    if key in memory:
        del memory[key]

        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=4)