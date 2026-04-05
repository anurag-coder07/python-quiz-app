"""Tests for the quiz engine."""

import unittest
from unittest.mock import patch

from quiz_app.engine import QuizEngine
from quiz_app.models import Question


class QuizEngineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.questions = [
            Question(
                category="Basics",
                prompt="Question 1",
                choices=["A", "B", "C", "D"],
                answer_index=1,
                explanation="Explanation 1",
            ),
            Question(
                category="Basics",
                prompt="Question 2",
                choices=["A", "B", "C", "D"],
                answer_index=2,
                explanation="Explanation 2",
            ),
            Question(
                category="Files",
                prompt="Question 3",
                choices=["A", "B", "C", "D"],
                answer_index=0,
                explanation="Explanation 3",
            ),
        ]
        self.engine = QuizEngine(self.questions)

    def test_submit_correct_answer_updates_score(self) -> None:
        result = self.engine.submit_answer(1)

        self.assertTrue(result.is_correct)
        self.assertEqual(self.engine.score, 1)
        self.assertEqual(self.engine.current_index, 1)

    def test_submit_wrong_answer_keeps_score_unchanged(self) -> None:
        result = self.engine.submit_answer(0)

        self.assertFalse(result.is_correct)
        self.assertEqual(result.correct_choice, "B")
        self.assertEqual(self.engine.score, 0)

    def test_category_breakdown_tracks_correct_answers(self) -> None:
        self.engine.submit_answer(1)
        self.engine.submit_answer(0)
        self.engine.submit_answer(0)

        self.assertEqual(
            self.engine.category_breakdown(),
            [("Basics", 1, 2), ("Files", 1, 1)],
        )

    def test_score_percentage_rounds_correctly(self) -> None:
        self.engine.submit_answer(1)
        self.engine.submit_answer(2)

        self.assertEqual(self.engine.score_percentage(), 67)

    @patch("quiz_app.engine.shuffle")
    def test_reset_can_shuffle_question_order(self, mock_shuffle) -> None:
        self.engine.reset(shuffle_questions=True)

        mock_shuffle.assert_called_once()


if __name__ == "__main__":
    unittest.main()
