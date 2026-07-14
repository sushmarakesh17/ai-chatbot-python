import streamlit as st
from datetime import datetime
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot Using Python")
st.write("Ask me anything about Python, AI, Machine Learning, or Data Science!")

# -----------------------------
# Chatbot Knowledge Base
# -----------------------------
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I'm doing great! Thanks for asking.",
    "your name": "I'm a Python AI Chatbot.",
    "python": "Python is a programming language widely used for AI, Data Science, and Web Development.",
    "ai": "AI stands for Artificial Intelligence.",
    "machine learning": "Machine Learning enables computers to learn from data.",
    "data science": "Data Science is the process of extracting insights from data.",
    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
    "bye": "Goodbye! Have a wonderful day!"
}

# -----------------------------
# Save Chat History
# -----------------------------
os.makedirs("output", exist_ok=True)

def save_chat(user_message, bot_message):
    with open("output/chat_history.txt", "a") as file:
        file.write(f"{datetime.now()} | You: {user_message}\n")
        file.write(f"{datetime.now()} | Bot: {bot_message}\n\n")

# -----------------------------
# User Input
# -----------------------------
user = st.text_input("You")

if st.button("Send"):

    if user.strip() == "":
        st.warning("Please enter a message.")

    else:

        user_lower = user.lower()

        found = False

        for key in sorted(responses.keys(), key=len, reverse=True):

            if key in user_lower:
                bot_response = responses[key]
                found = True
                break

        if not found:
            bot_response = "Sorry, I don't understand."

        st.success(bot_response)

        save_chat(user, bot_response)