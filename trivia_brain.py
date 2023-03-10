import html

'''
keep asking questions until reach end of data
calculate  score

'''
'''

# for question in questions:
#     answer = input(html.unescape(question['question']))  # To change back HTML Entities
#     score = 0
#     if answer == question['correct_answer']:
#         score = score + 1
#     print(score)

'''


class TriviaBrain:
    def __init__(self, list_of_questions):
        self.score = 0
        self.question_number = 0
        self.current_question = ""
        self.user_answer = ""
        self.question_list = list_of_questions

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        q_text = html.unescape(self.current_question['question'])
        self.question_number += 1
        return f"Q{self.question_number}:{q_text}"

    def check_answer(self, user_answer):
        if user_answer == self.current_question['correct_answer']:
            self.score += 1
            return True
        else:
            return False

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
