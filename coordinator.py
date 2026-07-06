import os

from dotenv import load_dotenv
from google import genai

from agents.memory import save_memory, get_memory, get_all_memory
from agents.task_agent import add_task, get_tasks
from agents.goal_agent import add_goal, get_goals

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def chat(user_message):

    lower = user_message.lower()

    # --------------------------
    # NAME MEMORY
    # --------------------------

    if "my name is" in lower:

        index = lower.find("my name is")
        name = user_message[index + len("my name is"):].strip()

        save_memory("name", name)

        return f"👋 Nice to meet you, {name}! I'll remember your name."

    if "what is my name" in lower or "who am i" in lower:

        name = get_memory("name")

        if name:
            return f"😊 Your name is {name}."

        return "I don't know your name yet. Tell me by saying 'My name is ...'"

    # --------------------------
    # SMART MEMORY
    # --------------------------

    if lower.startswith("remember "):

        fact = user_message[9:].strip()

        if "=" in fact:

            key, value = fact.split("=", 1)

            save_memory(key.strip(), value.strip())

            return f"🧠 I'll remember that {key.strip()} = {value.strip()}."

        return "Please use this format:\nRemember favorite_language = Python"

    if "what do you know about me" in lower:

        memory = get_all_memory()

        if not memory:
            return "I don't know anything about you yet."

        reply = "🧠 Here's what I know about you:\n\n"

        for key, value in memory.items():
            reply += f"• {key}: {value}\n"

        return reply

    # --------------------------
    # TASKS
    # --------------------------

    if lower.startswith("add task"):

        task = user_message[len("add task"):].strip()

        add_task(task)

        return f"✅ Task added:\n{task}"

    if "show my tasks" in lower or "list tasks" in lower:

        tasks = get_tasks()

        if not tasks:
            return "📋 You have no tasks."

        reply = "📋 Your Tasks\n\n"

        for i, task in enumerate(tasks, start=1):
            reply += f"{i}. {task}\n"

        return reply

    # --------------------------
    # GOALS
    # --------------------------

    if lower.startswith("add goal"):

        goal = user_message[len("add goal"):].strip()

        add_goal(goal)

        return f"🎯 Goal added:\n{goal}"

    if "show my goals" in lower or "list goals" in lower:

        goals = get_goals()

        if not goals:
            return "🎯 You have no goals."

        reply = "🎯 Your Goals\n\n"

        for i, goal in enumerate(goals, start=1):
            reply += f"{i}. {goal}\n"

        return reply

    # --------------------------
    # GEMINI
    # --------------------------

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message,
        )

        return response.text

    except Exception as e:

        return f"""⚠️ AI Service Error

{str(e)}

Please try again later.
"""