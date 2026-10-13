import requests
import json

response = requests.get(
    'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow'
)

questions = []

for data in response.json()['items']:
    question = {
        'title': data['title'],
        'link': data['link']
    }

    questions.append(question)

print(json.dumps(questions, indent=4))
