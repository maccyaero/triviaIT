import requests

response = requests.get(url="https://opentdb.com/api.php?amount=5&category=18&type=boolean")
response.raise_for_status()
'''
Create a list of questions
'''

questions = response.json()["results"]
print(questions)