# Professional Python Quiz App

This project is a polished command-line quiz application built entirely with Python. It is designed to look clean and professional on GitHub while still being simple enough for a beginner to understand and explain.

## Features

- Built only with Python
- Clean package structure
- 10 curated Python quiz questions
- Category-based score breakdown
- Instant answer feedback with explanations
- Best score saved locally between runs
- Basic test coverage using `unittest`

## Project Structure

```text
python-quiz-app/
|-- main.py
|-- README.md
|-- quiz_app/
|   |-- __init__.py
|   |-- application.py
|   |-- engine.py
|   |-- models.py
|   |-- question_bank.py
|   `-- storage.py
`-- tests/
    `-- test_engine.py
```

## How to Run

1. Open a terminal in the `python-quiz-app` folder.
2. Run:

```bash
python main.py
```

## How to Run Tests

```bash
python -m unittest discover -s tests
```

## Why This Project Is Good for GitHub

This repository shows:

- Python project organization
- clear separation of logic and user interface
- input validation and result tracking
- local data persistence
- documentation and test coverage

## Author

Created by Anurag with help from Codex.
