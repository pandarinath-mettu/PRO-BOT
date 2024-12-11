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

# Sidebar menu
st.sidebar.title("Menu")
menu = ["Home and Chat with Pro Bot", "Learn Python Syntax", "About"]
choice = st.sidebar.radio("Choose an option", menu)

# Load intents
intents = load_intents()

if choice == "Home and Chat with Pro Bot":
    st.header("Welcome to Pro Bot!")
    st.write("""
    Pro Bot is here to assist you in mastering Python programming. 
    Whether you're a beginner or looking to sharpen your skills, Pro Bot is your ideal programming companion.

    You can directly chat with Pro Bot here to ask programming-related questions, get answers instantly, or learn more about Python syntax.

    ### How to use:
    - **Ask Programming Questions**: Type your question in the text box below, and Pro Bot will help you with Python-related queries.
    - **Learn Python Syntax**: Select a Python topic from the menu to get detailed explanations.
    """)
    
    st.header("Chat with Pro Bot")
    user_input = st.text_input("You:", "")
    if user_input:
        response = get_response(user_input, intents)
        st.text_area("Pro Bot:", value=response, height=200)

elif choice == "Learn Python Syntax":
    st.header("Learn Python Syntax")
    topic = st.selectbox("Choose a Python Topic", [
        "Python Basics", "Input and Output in Python", "Data Types", 
        "Python Operators", "Conditional Statements in Python", 
        "Loops in Python - For, While and Nested Loops", 
        "Python Functions", "Python OOPs Concepts", "Python Modules", 
        "Python Exception Handling", "Python Collections Module", 
        "Python Packages", "Python Projects - Beginner to Advanced"
    ])
    
    def show_explanation(topic):
        if topic == "Python Basics":
            st.write("""
            **Python Basics**:
            Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used for web development, data analysis, automation, and more.
            - **Variables**: Used to store data.
            - **Indentation**: Python uses indentation to define blocks of code.
            - **Comments**: Written using `#` to explain the code.
            """)
        
        elif topic == "Input and Output in Python":
            st.write("""
            **Input and Output in Python**:
            Python allows you to take input from users and display output.
            - `input()` is used to take input from the user.
            - `print()` is used to display output to the user.
            Example:
            ```python
            name = input("Enter your name: ")
            print("Hello, " + name)
            ```
            """)

        elif topic == "Data Types":
            st.write("""
            **Data Types in Python**:
            Python has various data types such as:
            - **int**: Integer values.
            - **float**: Decimal numbers.
            - **str**: String values (text).
            - **list**: A collection of ordered items.
            - **tuple**: An immutable collection of ordered items.
            - **dict**: A collection of key-value pairs.
            - **bool**: Boolean values (`True` or `False`).
            """)

        elif topic == "Python Operators":
            st.write("""
            **Python Operators**:
            Operators are used to perform operations on variables and values.
            - **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%`
            - **Comparison Operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
            - **Logical Operators**: `and`, `or`, `not`
            - **Assignment Operators**: `=`, `+=`, `-=`, `*=`
            - **Membership Operators**: `in`, `not in`
            """)

        elif topic == "Conditional Statements in Python":
            st.write("""
            **Conditional Statements in Python**:
            Python uses `if`, `elif`, and `else` statements to perform conditional execution.
            Example:
            ```python
            x = 10
            if x > 5:
                print("Greater than 5")
            elif x == 5:
                print("Equal to 5")
            else:
                print("Less than 5")
            ```
            """)

        elif topic == "Loops in Python - For, While and Nested Loops":
            st.write("""
            **Loops in Python**:
            Loops allow you to repeat a block of code multiple times.
            - **For Loop**: Used to iterate over a sequence (like a list, tuple).
            - **While Loop**: Repeats as long as the condition is true.
            - **Nested Loops**: A loop inside another loop.
            Example:
            ```python
            for i in range(5):
                print(i)
            ```
            """)

        elif topic == "Python Functions":
            st.write("""
            **Python Functions**:
            Functions allow you to group code into reusable blocks.
            - Use `def` to define a function.
            Example:
            ```python
            def greet(name):
                print("Hello, " + name)
            greet("Alice")
            ```
            """)

        elif topic == "Python OOPs Concepts":
            st.write("""
            **Python OOPs Concepts**:
            Object-Oriented Programming (OOP) allows you to model real-world entities using classes and objects.
            - **Class**: A blueprint for creating objects.
            - **Object**: An instance of a class.
            - **Inheritance**, **Encapsulation**, **Polymorphism**, and **Abstraction** are key OOP concepts.
            """)

        elif topic == "Python Modules":
            st.write("""
            **Python Modules**:
            A module is a file containing Python code that can define functions, variables, and classes.
            - You can import a module using `import module_name`.
            Example:
            ```python
            import math
            print(math.sqrt(16))
            ```
            """)

        elif topic == "Python Exception Handling":
            st.write("""
            **Python Exception Handling**:
            Python uses `try`, `except`, and `finally` to handle errors in a graceful manner.
            Example:
            ```python
            try:
                x = 10 / 0
            except ZeroDivisionError:
                print("Cannot divide by zero!")
            ```
            """)

        elif topic == "Python Collections Module":
            st.write("""
            **Python Collections Module**:
            The `collections` module provides alternatives to built-in types like lists, tuples, and dictionaries.
            - **Counter**: A collection that counts elements.
            - **defaultdict**: A dictionary with default values.
            - **namedtuple**: A subclass of tuple with named fields.
            """)

        elif topic == "Python Packages":
            st.write("""
            **Python Packages**:
            A package is a collection of Python modules. You can install packages using `pip`.
            Example:
            ```bash
            pip install requests
            ```
            """)

        elif topic == "Python Projects - Beginner to Advanced":
            st.write("""
            **Python Projects - Beginner to Advanced**:
            - **Beginner**: Build a calculator, simple to-do list app, or a number guessing game.
            - **Intermediate**: Develop a web scraper, a weather app, or a blog application.
            - **Advanced**: Build machine learning models, web apps using Flask/Django, or a full-stack application.
            """)

    if st.button("Learn"):
        show_explanation(topic)

elif choice == "About":
    st.header("About Pro Bot")
    st.write("""
    **Pro Bot: Your Python Programming Assistant**

    The goal of this project is to create an interactive chatbot that assists users in learning and mastering Python programming.
    Built using Natural Language Processing (NLP) techniques, the chatbot can provide answers to various programming questions, explain Python syntax, and offer advice on best practices.

    **Key Components:**
    - **NLP and Machine Learning**: Pro Bot uses NLP to analyze user input and classify it into predefined intents. It also uses machine learning techniques to provide relevant responses based on the input.
    - **Streamlit Interface**: Streamlit is used to create an interactive and user-friendly interface where users can type their questions and get answers from the chatbot in real-time.

    **Key Features of Pro Bot:**
    - Answering Python programming questions.
    - Explaining Python syntax and concepts.
    - Offering code examples and debugging tips.
    - Providing interactive lessons for learning Python topics.

    **Dataset:**
    The dataset includes intents related to various Python topics such as variables, loops, functions, conditions, and classes. Each intent consists of patterns (user queries) and responses that the bot can use to generate helpful answers.

    **Conclusion:**
    Pro Bot is a beginner-friendly chatbot that helps users learn Python programming in a simple and interactive manner. The bot's purpose is to provide quick answers to questions, offer explanations of Python concepts, and help improve programming skills.
    """)
