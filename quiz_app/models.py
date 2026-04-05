"""Data models for the quiz application."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    """Represents a single quiz question."""

    category: str
    prompt: str
    choices: list[str]
    answer_index: int
    explanation: str


@dataclass(frozen=True)
class AnswerResult:
    """Represents the result of a submitted answer."""

    question: Question
    selected_index: int
    is_correct: bool

    @property
    def correct_choice(self) -> str:
        return self.question.choices[self.question.answer_index]
