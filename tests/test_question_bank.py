"""Tests for the question bank."""

import unittest

from quiz_app.question_bank import load_questions


class QuestionBankTests(unittest.TestCase):
    def test_load_questions_returns_question_objects(self) -> None:
        questions = load_questions()

        self.assertEqual(len(questions), 10)
        self.assertTrue(all(question.prompt for question in questions))
        self.assertTrue(all(question.choices for question in questions))


if __name__ == "__main__":
    unittest.main()
