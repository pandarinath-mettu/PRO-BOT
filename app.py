import streamlit as st
import json
import random

# Load intents
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

# Main app
st.title("Pro Bot: Your Python Programming Assistant")
st.sidebar.title("Menu")
menu = ["Chat with Pro Bot", "Learn Python Syntax"]
choice = st.sidebar.radio("Choose an option", menu)

# Load intents
intents = load_intents()

if choice == "Chat with Pro Bot":
    st.header("Chat with Pro Bot")
    user_input = st.text_input("You:", "")
    if user_input:
        response = get_response(user_input, intents)
        st.text_area("Pro Bot:", value=response, height=200)

elif choice == "Learn Python Syntax":
    st.header("Learn Python Syntax")
    topic = st.selectbox("Choose a Python Topic", ["Variables", "Loops", "Functions", "Conditions", "Classes"])
    if st.button("Learn"):
        for intent in intents:
            if intent["tag"] == f"python_{topic.lower()}":
                st.write(random.choice(intent["responses"]))
