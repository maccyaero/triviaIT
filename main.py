import tkinter as tk
import requests

# Fetch Data from API
response = requests.get(url="https://opentdb.com/api.php?amount=5&category=18&type=boolean")
response.raise_for_status()
# Create a list of questions
print(response.json())

questions = response.json()["results"]
print(questions)
# Game Logic
# Ask User the Question unil run out of questions.
# When run out the fetch new ones again.
# If user is correct add 1 to score.
# If user is wrong then ask next question
for question in questions:
    answer = input(question['question'])
    score = 0
    if answer == question['correct_answer']:
        score = score + 1
    print(score)

# If user closes the window then do not throw an error but just raise exception
