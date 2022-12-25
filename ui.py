from tkinter import *
from trivia_brain import TriviaBrain

THEME_COLOR = "#375362"


class TriviaInterface:

    def __init__(self, quiz_brain: TriviaBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("IT Quiz")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        # Create a label widget
        self.score_label = Label(self.window, text=f"Score:{self.quiz.score}", background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Create a canvas where the questions will show up
        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question goes here", width=250,
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Load image files using the PhotoImage class for the true and false buttons
        true_icon = PhotoImage(file="images/true.png")
        false_icon = PhotoImage(file="images/false.png")

        # Create the true and false button widgets
        self.true_button = Button(self.window, image=true_icon, command=self.true_pressed)
        self.false_button = Button(self.window, image=false_icon, command=self.false_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Thanks for playing. "
                                                            f"You got {self.quiz.score}/5 questions right.")

            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score_label.config(text=f"Score: {self.quiz.score}")

        else:
            self.canvas.config(bg='red')
        self.window.after(100, self.get_next_question)
