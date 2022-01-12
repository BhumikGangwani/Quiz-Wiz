class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # Checks if the quiz has remaining questions
    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    # Returns an f-string of the next question in the question_bank
    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    # Checks if the user selected the correct answer
    def check_answer(self, user_answer: str) -> bool:
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        return False
