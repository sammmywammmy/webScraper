from requests import *
from bs4 import BeautifulSoup

url = "https://www.horoscope.com/us/games/quiz/game-quiz-are-you-good-or-evil.aspx"
getURL = get(url)
getText = getURL.text
plain_text = getURL.text.encode('ascii', 'replace')
soup = BeautifulSoup(plain_text, "html.parser")
question = soup.select('h3')[0].text.strip()

print(question)