def handle_query(query):
    # Simple keyword-based logic
    keywords = {
        "python": "Python is a versatile language great for beginners.",
        "java": "Java is a popular object-oriented programming language.",
        "debugging": "Debugging is the process of identifying and fixing issues in your code."
    }

    for keyword, response in keywords.items():
        if keyword.lower() in query.lower():
            return response
    
    return "Sorry, I don't have information on that topic. Try asking another question."
