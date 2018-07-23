import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://quizlet.com/5046711/test" + str(page)
        source_code = requests.get(url, allow_redirects = False) #just grabbing hmtl code
        plain_text = source_code.text.encode("ascii","replace")
        soup = BeautifulSoup(plain_text, "html.parser")
        for question in soup.findAll("a", {"class": "user-name"}):
            href = link.get("href")
            question = link.string
        for answer in soup.findAll("a", {"class": ""})
            print(href)
            print(question)
        #page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"lxml")
    # if you want to gather photos from that user
    for quizAnswers in soup.findAll('span', {'class': 'TermText notranslate lang-en'}): # all photos of the user
        quizAnswers='https://thenewboston.com'+item_name.get('src')
        print(quizAnswers)
    # if you want to gather links for a web crawler
  """"  for questions in soup.findAll(''):
        href = link.get('href')
        print(questions)""""


trade_spider(1)
