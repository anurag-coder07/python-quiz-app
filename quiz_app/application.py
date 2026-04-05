"""Console interface for the quiz application."""

from quiz_app.engine import QuizEngine
from quiz_app.question_bank import QUESTIONS
from quiz_app.storage import load_best_score, save_best_score


class QuizApplication:
    """Runs the interactive console quiz."""

    def __init__(self) -> None:
        self.engine = QuizEngine(QUESTIONS)

    def run(self) -> None:
        self._print_welcome()

        while True:
            self.engine.reset()
            self._run_quiz_round()
            if not self._ask_to_play_again():
                print("\nThanks for using the quiz app.")
                break

    def _print_welcome(self) -> None:
        print("=" * 62)
        print(" " * 22 + "Python Quiz App")
        print("=" * 62)
        print("Answer the questions and check your score at the end.")
        print(f"Questions available: {self.engine.total_questions}")
        print("Type the option number for each answer.")
        print(f"Best recorded score: {load_best_score()}%")

    def _run_quiz_round(self) -> None:
        while self.engine.has_more_questions:
            question = self.engine.current_question
            question_number = self.engine.current_index + 1

            print("\n" + "-" * 62)
            print(f"Question {question_number} of {self.engine.total_questions}")
            print(f"Category: {question.category}")
            print(question.prompt)

            for option_number, choice in enumerate(question.choices, start=1):
                print(f"  {option_number}. {choice}")

            selected_index = self._get_user_choice(len(question.choices))
            result = self.engine.submit_answer(selected_index)

            if result.is_correct:
                print("Result: Correct")
            else:
                print(f"Result: Incorrect. Correct answer: {result.correct_choice}")

            print(f"Why it matters: {result.question.explanation}")

        self._print_summary()

    def _print_summary(self) -> None:
        percentage = self.engine.score_percentage()
        best_score = save_best_score(percentage)

        print("\n" + "=" * 62)
        print("Quiz Summary")
        print("=" * 62)
        print(f"Score: {self.engine.score}/{self.engine.total_questions}")
        print(f"Accuracy: {percentage}%")
        print(self.engine.performance_message())
        print(f"Best score so far: {best_score}%")
        print("\nCategory Breakdown:")

        for category, correct, total in self.engine.category_breakdown():
            print(f"- {category}: {correct}/{total}")

    def _get_user_choice(self, total_choices: int) -> int:
        while True:
            user_input = input("Choose an option number: ").strip()

            if not user_input.isdigit():
                print("Please enter a number only.")
                continue

            choice_number = int(user_input)
            if 1 <= choice_number <= total_choices:
                return choice_number - 1

            print(f"Please choose a number between 1 and {total_choices}.")

    def _ask_to_play_again(self) -> bool:
        while True:
            answer = input("\nWould you like to play again? (y/n): ").strip().lower()
            if answer in {"y", "yes"}:
                return True
            if answer in {"n", "no"}:
                return False
            print("Please type y or n.")
