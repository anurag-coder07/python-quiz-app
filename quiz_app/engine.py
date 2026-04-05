"""Core quiz logic and scoring."""

from collections import Counter
from random import shuffle

from quiz_app.models import AnswerResult, Question


class QuizEngine:
    """Manages quiz progress, scoring, and reporting."""

    def __init__(self, questions: list[Question]) -> None:
        if not questions:
            raise ValueError("QuizEngine requires at least one question.")

        self._question_bank = list(questions)
        self._category_totals = Counter(question.category for question in self._question_bank)
        self.reset()

    def reset(self, shuffle_questions: bool = False) -> None:
        self.current_index = 0
        self.score = 0
        self._category_correct = Counter()
        self.history: list[AnswerResult] = []
        self._questions = list(self._question_bank)

        if shuffle_questions:
            shuffle(self._questions)

    @property
    def total_questions(self) -> int:
        return len(self._questions)

    @property
    def has_more_questions(self) -> bool:
        return self.current_index < self.total_questions

    @property
    def current_question(self) -> Question:
        if not self.has_more_questions:
            raise IndexError("There are no more questions in the quiz.")
        return self._questions[self.current_index]

    def submit_answer(self, selected_index: int) -> AnswerResult:
        question = self.current_question
        is_correct = selected_index == question.answer_index

        if is_correct:
            self.score += 1
            self._category_correct[question.category] += 1

        result = AnswerResult(
            question=question,
            selected_index=selected_index,
            is_correct=is_correct,
        )
        self.history.append(result)
        self.current_index += 1
        return result

    def score_percentage(self) -> int:
        return round((self.score / self.total_questions) * 100)

    def answered_questions(self) -> int:
        return len(self.history)

    def category_breakdown(self) -> list[tuple[str, int, int]]:
        return [
            (
                category,
                self._category_correct[category],
                total,
            )
            for category, total in self._category_totals.items()
        ]

    def performance_message(self) -> str:
        percentage = self.score_percentage()
        if percentage >= 90:
            return "Excellent performance. Your Python fundamentals look strong."
        if percentage >= 70:
            return "Good work. You have a solid base and clear momentum."
        return "Promising start. Review the explanations and try again for a stronger score."
