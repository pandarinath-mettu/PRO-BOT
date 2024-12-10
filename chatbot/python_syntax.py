def teach_python_syntax(topic):
    python_syntax = {
        "variables": (
            "In Python, you can create a variable by assigning a value to a name:\n"
            "e.g. x = 10\n"
            "Variables can hold different data types like integers, floats, strings, etc."
        ),
        "loops": (
            "Python has two main types of loops: 'for' and 'while'.\n"
            "For example:\n"
            "for i in range(5):\n"
            "    print(i)\n"
            "While loop example:\n"
            "x = 0\n"
            "while x < 5:\n"
            "    print(x)\n"
            "    x += 1"
        ),
        "functions": (
            "Functions are defined using the 'def' keyword:\n"
            "def my_function():\n"
            "    print('Hello, World!')\n"
            "You can call the function using its name:\n"
            "my_function()"
        ),
        "conditions": (
            "Python uses 'if', 'elif', and 'else' for conditional logic:\n"
            "if x > 10:\n"
            "    print('x is greater than 10')\n"
            "elif x == 10:\n"
            "    print('x is equal to 10')\n"
            "else:\n"
            "    print('x is less than 10')"
        ),
        "classes": (
            "Python supports Object-Oriented Programming (OOP). You can create classes using the 'class' keyword:\n"
            "class MyClass:\n"
            "    def __init__(self, value):\n"
            "        self.value = value\n"
            "    def display(self):\n"
            "        print(self.value)\n"
            "To create an object of the class:\n"
            "obj = MyClass(10)\n"
            "obj.display()"
        ),
    }
    
    return python_syntax.get(topic.lower(), "Sorry, I don't have information on that topic.")
