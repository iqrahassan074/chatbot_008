import streamlit as st

st.set_page_config(page_title="🤖 ChatyBot", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .user-bubble {
        background-color: #A3E4D7;
        color: #000;
        padding: 12px;
        border-radius: 15px;
        margin: 8px 0;
        text-align: right;
        width: fit-content;
        margin-left: auto;
        font-size: 16px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .bot-bubble {
        background-color: #F8F9F9;
        color: #000;
        padding: 12px;
        border-radius: 15px;
        margin: 8px 0;
        width: fit-content;
        margin-right: auto;
        font-size: 16px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .chat-container {
        max-height: 450px;
        overflow-y: auto;
        padding: 5px;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        color: gray;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

qa_pairs = {
    "hello": "Hi there! 👋 How can I help you today?",
    "how are you": "I'm just a bunch of Python code, but I'm feeling great! 😄",
    "what is your name": "You can call me ChatyBot 🤖",
    "who made you": "I was created using Streamlit with love! 💻✨",
    "what is python": "🐍 Python is a popular programming language known for simplicity and power.",
    "tell me a joke": "Why did the programmer quit his job? Because he didn’t get arrays! 😂",
    "bye": "Goodbye! 👋 Have a great day!",
    "thank you": "You're welcome! 😊",
    "what can you do": "I can answer questions and brighten your day with emojis! 🌟",
    "what is ai": "AI stands for Artificial Intelligence 🤖 — machines that can learn and think!",
    "what is streamlit": "Streamlit is a Python framework for building beautiful web apps easily! 🚀",
    "who are you": "I'm ChatyBot 🤖, your friendly Q&A assistant!",
    "what's your purpose": "To chat, help, and sprinkle some emoji magic! ✨"
}

st.markdown("<h1 style='text-align: center;'>🤖 Chat with ChatyBot</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state.messages:
        bubble_class = "user-bubble" if msg["role"] == "user" else "bot-bubble"
        st.markdown(f'<div class="{bubble_class}">{msg["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

form = st.form("chat_form", clear_on_submit=True)
input_col, submit_col = form.columns([5, 1])
user_input = input_col.text_input("Type your message...", label_visibility="collapsed")
submit = submit_col.form_submit_button("Send")

if submit and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input})
    reply = "🤔 I'm not sure how to answer that. Try asking something else!"
    for question, answer in qa_pairs.items():
        if question in user_input.lower():
            reply = answer
            break
    st.session_state.messages.append({"role": "bot", "content": reply})

st.markdown('<div class="footer">Made by Iqra Hassan 💖</div>', unsafe_allow_html=True)
