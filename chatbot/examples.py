def get_code_example(language):
    examples = {
        "python": "def hello_world():\n    print('Hello, World!')",
        "java": "public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println('Hello, World!');\n    }\n}",
        "c++": "#include <iostream>\nusing namespace std;\nint main() {\n    cout << 'Hello, World!' << endl;\n    return 0;\n}"
    }
    return examples.get(language.lower(), "Example not available for this language.")
