import streamlit as st
import json
import random
import datetime
import csv

# Load intents
@st.cache
def load_intents():
    with open("intents.json", "r") as file:
        return json.load(file)

# Get response from the bot
def get_response(user_input, intents):
    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input.lower():
                return random.choice(intent["responses"])
    return "I'm not sure about that. Can you rephrase your question?"

# Save chat history to a CSV file
def save_chat_history(user_input, response):
    if not os.path.exists("chat_log.csv"):
        with open("chat_log.csv", "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["User Input", "Pro Bot Response", "Timestamp"])

    with open("chat_log.csv", "a", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        csv_writer.writerow([user_input, response, timestamp])

# Main app
def main():
    st.title("Pro Bot: Your Python Programming Assistant")
    st.sidebar.title("Menu")
    menu = ["Chat with Pro Bot", "Learn Python Syntax", "Conversation History", "About"]
    choice = st.sidebar.radio("Choose an option", menu)

    # Load intents
    intents = load_intents()

    if choice == "Chat with Pro Bot":
        st.header("Chat with Pro Bot")
        st.write("**Ask Pro Bot anything about Python programming!**")
        user_input = st.text_input("You:", "")

        if user_input:
            response = get_response(user_input, intents)
            st.text_area("Pro Bot:", value=response, height=200)

            save_chat_history(user_input, response)

    elif choice == "Learn Python Syntax":
        st.header("Learn Python Syntax")
        topic = st.selectbox("Choose a Python Topic", ["Variables", "Loops", "Functions", "Conditions", "Classes"])
        if st.button("Learn"):
            for intent in intents:
                if intent["tag"] == f"python_{topic.lower()}":
                    st.write(random.choice(intent["responses"]))

    elif choice == "Conversation History":
        st.header("Conversation History")
        if os.path.exists("chat_log.csv"):
            with open("chat_log.csv", "r", encoding="utf-8") as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)
                for row in csv_reader:
                    st.text(f"User: {row[0]}")
                    st.text(f"Pro Bot: {row[1]}")
                    st.text(f"Timestamp: {row[2]}")
                    st.markdown("---")
        else:
            st.write("No conversation history found.")

    elif choice == "About":
        st.header("About Pro Bot")
        st.write("Pro Bot is your friendly Python programming assistant designed to help you learn Python, answer your queries, and make programming fun and engaging.")
        st.write("This bot is built using NLP techniques and a simple intent-matching algorithm, and the interactive interface is powered by Streamlit.")

if __name__ == "__main__":
    main()
