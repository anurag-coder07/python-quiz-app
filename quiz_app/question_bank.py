"""Question bank for the Python quiz application."""

from quiz_app.models import Question


QUESTIONS: list[Question] = [
    Question(
        category="Python Basics",
        prompt="Which keyword is used to define a function in Python?",
        choices=["func", "define", "def", "lambda"],
        answer_index=2,
        explanation="Python uses the `def` keyword to create a named function."
    ),
    Question(
        category="Python Basics",
        prompt="Which data type stores key-value pairs in Python?",
        choices=["list", "tuple", "set", "dict"],
        answer_index=3,
        explanation="A dictionary stores values by keys, which makes it ideal for lookup-based data."
    ),
    Question(
        category="Control Flow",
        prompt="What does an `if` statement do in Python?",
        choices=[
            "Repeats a block forever",
            "Checks a condition and decides which code to run",
            "Imports another file",
            "Converts text into numbers"
        ],
        answer_index=1,
        explanation="An `if` statement runs code only when its condition evaluates to true."
    ),
    Question(
        category="Data Structures",
        prompt="Which Python collection is ordered and mutable?",
        choices=["list", "tuple", "set", "frozenset"],
        answer_index=0,
        explanation="Lists preserve order and allow items to be changed, added, or removed."
    ),
    Question(
        category="Data Structures",
        prompt="Which method adds a single item to the end of a list?",
        choices=["extend()", "append()", "insert()", "push()"],
        answer_index=1,
        explanation="`append()` adds exactly one item to the end of a list."
    ),
    Question(
        category="Functions",
        prompt="What is returned by a Python function when there is no explicit `return` statement?",
        choices=["0", "False", "An empty string", "None"],
        answer_index=3,
        explanation="Python functions return `None` by default when no value is explicitly returned."
    ),
    Question(
        category="Error Handling",
        prompt="Which keyword is used to handle exceptions in Python?",
        choices=["catch", "except", "handle", "rescue"],
        answer_index=1,
        explanation="Python uses `except` inside a `try` block to handle exceptions."
    ),
    Question(
        category="Files",
        prompt="Which mode opens a file for reading in Python?",
        choices=["r", "w", "a", "x"],
        answer_index=0,
        explanation="The `r` mode opens a file for reading."
    ),
    Question(
        category="Object-Oriented Python",
        prompt="What does `self` usually represent inside a class method?",
        choices=[
            "The Python interpreter",
            "The current instance of the class",
            "The parent class only",
            "A built-in debugging tool"
        ],
        answer_index=1,
        explanation="`self` refers to the current object instance, allowing access to its data and methods."
    ),
    Question(
        category="Best Practices",
        prompt="Why is input validation important in a Python app?",
        choices=[
            "It makes code longer without benefit",
            "It removes the need for testing",
            "It helps prevent invalid data from causing bugs",
            "It replaces documentation"
        ],
        answer_index=2,
        explanation="Input validation improves reliability and protects the app from bad or unexpected values."
    )
]
