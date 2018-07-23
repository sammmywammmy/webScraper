# import libraries
import requests
from bs4 import BeautifulSoup

quizPage = "http://www.funtrivia.com/playquiz/quiz18138014c52e8.html"
response = requests.get("http://www.funtrivia.com/playquiz/quiz18138014c52e8.html")
soup = BeautifulSoup(response.content, "html.parser")
print(quizPage)


