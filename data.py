import json
import requests
number_of_question = int(input("Enter the number of question you want : "))

url = f'https://opentdb.com/api.php?amount={number_of_question}&category=18&difficulty=easy&type=boolean'
response = requests.get(url)
data = response.text
arranged_data = json.loads(data)

question_data = arranged_data["results"]


#https://opentdb.com/api_config.php





