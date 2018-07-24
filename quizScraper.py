# import libraries
import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.funtrivia.com/playquiz/quiz18138014c52e8.html")
soup = BeautifulSoup(response.content, "html.parser")

question = soup.find("b")
#quizq = question.text.strip()
print(question)

