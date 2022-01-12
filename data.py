import requests
import html

NO_OF_QUESTIONS = 25
CATEGORY: int  # To generate questions from a specific category
TYPE = "boolean"  # Constant whose value should not be changed

parameters = {
    "amount": NO_OF_QUESTIONS,
    "category": 22,
    "type": TYPE,
}

# Accesses the Open Trivia DB API to generate questions for the quiz.
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
for question in question_data:
    question["question"] = html.unescape(question["question"])
