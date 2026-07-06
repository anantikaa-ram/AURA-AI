# 🤖 AURA AI

## Intelligent Multi-Agent Personal Assistant

AURA AI is a multi-agent personal assistant built using Google's Gemini 2.5 Flash model and Streamlit. It combines conversational AI with persistent memory, task management, goal tracking, PDF intelligence, and web search into a single application.

---

# Features

### 🧠 Smart Memory
- Remembers user information
- Stores key-value memories
- Recalls saved information

### 📋 Task Management
- Add tasks
- View tasks
- Persistent task storage

### 🎯 Goal Management
- Add goals
- Track goals
- Persistent goal storage

### 📄 PDF Intelligence
- Upload PDF documents
- Ask questions about uploaded PDFs
- AI-generated answers using Gemini

### 🌐 Web Search
- Search the web directly from AURA

### 💬 AI Chat
- Natural conversation using Gemini 2.5 Flash

---

# Architecture

```
User
   │
   ▼
Streamlit UI
   │
   ▼
Coordinator Agent
   │
   ├──────── Memory Agent
   ├──────── Task Agent
   ├──────── Goal Agent
   ├──────── PDF Agent
   └──────── Web Agent
           │
           ▼
     Gemini 2.5 Flash
```

---

# Technologies Used

- Python
- Streamlit
- Google Gemini 2.5 Flash
- PyPDF
- DuckDuckGo Search
- JSON Storage
- Python Dotenv

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AURA-AI.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# Project Structure

```
AURA-AI
│
├── agents
│   ├── coordinator.py
│   ├── memory.py
│   ├── task_agent.py
│   ├── goal_agent.py
│   ├── pdf_agent.py
│   ├── web_agent.py
│   └── planner.py
│
├── app.py
├── main.py
├── memory.json
├── tasks.json
├── requirements.txt
└── README.md
```

---

# Future Improvements

- Voice Assistant
- Calendar Integration
- Email Automation
- Multi-language Support
- Cloud Database
- Authentication
- Mobile Version

---

# Author

**Anantikaa Ramesh **

Built as part of the **Kaggle AI Agents: Intensive Vibe Coding Capstone Project with Google**.
