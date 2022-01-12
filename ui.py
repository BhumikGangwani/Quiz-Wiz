from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"  # Value can be changed with preference. Should be hex code.


class QuizUI:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        # Window
        self.window = Tk()
        self.window.title(string="THIS IS THE TITLE")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=2, column=1)

        # Labels
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    # Displays the next question on the window. If all questions are answered, ends the quiz.
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.true_button.config(state="active")
            self.false_button.config(state="active")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f'You\'ve completed the quiz\n'
                                        f'Your final score was: {self.quiz.score}/{self.quiz.question_number}')
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # Checks if the answer for the current question is True
    def check_true(self):
        result = self.quiz.check_answer("True")
        self.flash_answer(result)

    # Checks if the answer for the current question is False
    def check_false(self):
        result = self.quiz.check_answer("False")
        self.flash_answer(result)

    # Improves UI by flashing green for correct answer and red for wrong answer
    def flash_answer(self, result: bool):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        if result:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(ms=1000, func=self.get_next_question)
