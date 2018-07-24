import requests
from bs4 import BeautifulSoup

def questions(max_pages):
    page = 1

    while page <= max_pages:
        url = "https://www.horoscope.com/us/games/quiz/game-quiz-whats-in-your-immediate-future.aspx" + str(page)
        getURL = requests.get(url, allow_redirects=False)
        plain_text = getURL.text.encode('ascii', 'replace') #convert to plain text
        soup = BeautifulSoup(plain_text, "html.parser") #parse plain text

        question = soup.select('h3')
        print(question)

        page += 1

questions(1)

