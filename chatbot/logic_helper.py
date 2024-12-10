def explain_logic(topic):
    explanations = {
        "binary search": (
            "Binary search is an efficient algorithm for finding an item in a sorted list. "
            "It works by repeatedly dividing the search interval in half. Complexity: O(log n)."
        ),
        "merge sort": (
            "Merge sort is a divide-and-conquer algorithm that splits the array into halves, "
            "sorts each half, and then merges them back together. Complexity: O(n log n)."
        )
    }
    return explanations.get(topic.lower(), "Sorry, I don't have an explanation for that topic.")
