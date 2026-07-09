from datetime import datetime

# ==========================
# Welcome Message
# ==========================
print("=" * 50)
print("        Welcome to AI Chatbot")
print("=" * 50)

print("\nI can answer questions about:")
print("- Python")
print("- AI")
print("- Machine Learning")
print("- Data Science")
print("- Greetings")
print("- How are you")
print("- My name")
print("- Thank you")
print("Type 'bye' to exit.\n")

# ==========================
# Chatbot Knowledge Base
# ==========================
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

# ==========================
# Function to Save Chat History
# ==========================
def save_chat(user_message, bot_message):
    with open("output/chat_history.txt", "a") as file:
        file.write(f"{datetime.now()} | You: {user_message}\n")
        file.write(f"{datetime.now()} | Bot: {bot_message}\n\n")

# ==========================
# Chat Loop
# ==========================
while True:

    user = input("You: ").strip().lower()

    # Exit condition
    if user == "bye":
        bot_response = responses["bye"]
        print("Bot:", bot_response)
        save_chat(user, bot_response)
        break

    found = False

    # Check longest keywords first
    for key in sorted(responses.keys(), key=len, reverse=True):

        if key in user:
            bot_response = responses[key]
            print("Bot:", bot_response)
            save_chat(user, bot_response)
            found = True
            break

    # Default response
    if not found:
        bot_response = "Sorry, I don't understand."
        print("Bot:", bot_response)
        save_chat(user, bot_response)
        
