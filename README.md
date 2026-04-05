# Python CLI Quiz App

A command-line quiz app built with Python. It asks multiple-choice questions, checks answers, and shows a summary at the end of each round.

## What Problem It Solves

This project solves the problem of making quiz practice more interactive than a plain question list. Instead of only showing questions and answers, it tracks the score, shows categories, reviews answers, and lets the user replay the quiz.

## What I Learned

I built this project to practice Python program structure, question handling, score tracking, and user interaction in the terminal. It also helped me work with lists, dictionaries, functions, loops, and modular file organization.

## Features

- Multiple questions
- Categories for questions
- Score tracking
- Correct answers shown after each round
- Performance message based on final score
- Replay option
- instant feedback after each answer
- final score summary
- score by category
- best score saved locally
- clean terminal output
- input retry for invalid answers
- modular structure with separate files
- question bank stored in a separate list/dictionary structure
- random question order each round

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
    |-- test_engine.py
    |-- test_question_bank.py
    `-- test_storage.py
```

## How to Run

1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```

## How to Use

1. Start the app.
2. Read each question carefully.
3. Enter the option number for your answer.
4. Check the explanation shown after each answer.
5. Watch your score update as you answer questions.
6. Review your final score, category breakdown, and answer review.
7. Choose whether to play another round.

## Example

```text
==============================================================
                      Python Quiz App
==============================================================
Answer the questions and check your score at the end.
Questions available: 10
Type the option number for each answer.
Question order changes each round.
Best recorded score: 0%

--------------------------------------------------------------
Question 1 of 10
Category: Python Basics
Which keyword is used to define a function in Python?
  1. func
  2. define
  3. def
  4. lambda
Choose an option number: 3
Result: Correct
Current score: 1/1

==============================================================
Quiz Summary
==============================================================
Score: 8/10
Accuracy: 80%
Good work. You have a solid base and clear momentum.

Answer Review:
1. Which keyword is used to define a function in Python?
   Your answer: def
   Correct answer: def
   Status: Correct
```

## Tests

```bash
python -m unittest discover -s tests
```

## Concepts Used

- Lists & dictionaries
- Functions
- Loops
