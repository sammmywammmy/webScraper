from requests import *
from bs4 import BeautifulSoup

url = "https://www.horoscope.com/us/games/quiz/game-quiz-are-you-good-or-evil.aspx"
getURL = get(url)
getText = getURL.text
soup = BeautifulSoup(getText, "html.parser")

question = soup.select('h3')[0].text.strip()
print(question)

