import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

from agents.coordinator import chat
from agents.memory import get_memory
from agents.task_agent import get_tasks
from agents.goal_agent import get_goals
from agents.pdf_agent import read_pdf

# ----------------------------
# GEMINI
# ----------------------------

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# ----------------------------
# PAGE
# ----------------------------

st.set_page_config(
    page_title="AURA AI",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# CSS
# ----------------------------

st.markdown("""
<style>

.stApp{
    background:#0d1117;
}

h1,h2,h3{
    color:white;
}

.card{
    background:#161b22;
    padding:20px;
    border-radius:15px;
    color:white;
    margin-bottom:20px;
    border:1px solid #30363d;
}

.chatbox{
    background:#161b22;
    padding:15px;
    border-radius:15px;
    margin-bottom:10px;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# TITLE
# ----------------------------

st.title("🤖 AURA AI")
st.caption("Your Personal Intelligent Assistant")

left, center, right = st.columns([1,2,1])

# ====================================================
# LEFT PANEL
# ====================================================

with left:

    name = get_memory("name")
    tasks = get_tasks()
    goals = get_goals()

    st.markdown(f"""
    <div class='card'>
    <h3>🧠 Memory</h3>
    <p><b>Name:</b> {name if name else "Not Set"}</p>
    </div>
    """, unsafe_allow_html=True)

    task_html = "<br>".join(
        [f"✅ {task}" for task in tasks]
    )

    st.markdown(f"""
    <div class='card'>
    <h3>📋 Tasks ({len(tasks)})</h3>
    <p>{task_html if tasks else "No tasks added."}</p>
    </div>
    """, unsafe_allow_html=True)

    goal_html = "<br>".join(
        [f"🎯 {goal}" for goal in goals]
    )

    st.markdown(f"""
    <div class='card'>
    <h3>🎯 Goals ({len(goals)})</h3>
    <p>{goal_html if goals else "No goals added."}</p>
    </div>
    """, unsafe_allow_html=True)

# ====================================================
# CHAT
# ====================================================

with center:

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:

        if msg["role"] == "user":

            st.markdown(
                f"<div class='chatbox'>👤 <b>You</b><br>{msg['content']}</div>",
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"<div class='chatbox'>🤖 <b>AURA</b><br>{msg['content']}</div>",
                unsafe_allow_html=True
            )

    prompt = st.chat_input("Ask AURA anything...")

    if prompt:

        st.session_state.messages.append(
            {
                "role":"user",
                "content":prompt
            }
        )

        reply = chat(prompt)

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":reply
            }
        )

        st.rerun()

# ====================================================
# RIGHT PANEL
# ====================================================

with right:

    st.markdown("""
    <div class='card'>
    <h3>⚡ Status</h3>
    <p>🟢 Online</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card'>
    <h3>📊 Statistics</h3>
    <p>🧠 Memory: {"Active" if name else "Empty"}</p>
    <p>📋 Tasks: {len(tasks)}</p>
    <p>🎯 Goals: {len(goals)}</p>
    </div>
    """, unsafe_allow_html=True)

    # ===============================
    # PDF CHAT
    # ===============================

    st.markdown("## 📄 PDF Assistant")

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_pdf:

        pdf_text = read_pdf(uploaded_pdf)

        st.success("✅ PDF Loaded Successfully")

        question = st.text_input(
            "Ask a question about the PDF"
        )

        if question:

            with st.spinner("AURA is reading the PDF..."):

                prompt = f"""
You are an AI assistant.

Answer ONLY using the PDF below.

PDF:

{pdf_text}

Question:

{question}
"""

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                st.success(response.text)

    st.markdown("""
    <div class='card'>
    <h3>🚀 Version</h3>
    <p>AURA v1.0</p>
    </div>
    """, unsafe_allow_html=True)