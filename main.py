from ui import TriviaInterface
from data import questions
from trivia_brain import TriviaBrain

quiz = TriviaBrain(questions)
quiz_ui = TriviaInterface(quiz)
# ---------------------------- CREATE USER INTERFACE  ------------------------------- #

# trivia_ui = TriviaInterface()

# ---------------------------- FETCH DATA FROM API  ------------------------------- #


# ---------------------------- Game Logic ------------------------------- #
'''
Ask User the Question until run out of questions.
When run out the fetch new ones again.
If user is correct add 1 to score.
If user is wrong then ask next question

If user closes the window then do not throw an error but just raise exception
'''
