import json
import os

GOAL_FILE = "goals.json"


def load_goals():
    if os.path.exists(GOAL_FILE):
        with open(GOAL_FILE, "r") as f:
            return json.load(f)
    return []


goals = load_goals()


def save_goals():
    with open(GOAL_FILE, "w") as f:
        json.dump(goals, f, indent=4)


def add_goal(goal):
    goals.append(goal)
    save_goals()


def get_goals():
    return goals