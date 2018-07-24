from requests import *
from bs4 import BeautifulSoup
import re

url = "https://www.horoscope.com/us/games/quiz/game-quiz-are-you-good-or-evil.aspx"
getURL = get(url)
getText = getURL.text
plain_text = getURL.text.encode('ascii', 'replace')
soup = BeautifulSoup(plain_text, "html.parser")

question_containers = soup.findAll(['h3'])
firstQuestion = question_containers[0]
firstQ = firstQuestion.text
print(firstQ)

#for q in soup.findAll(["h3"]):
  #  questions = q.
   # print (questions)
