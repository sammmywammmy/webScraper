import requests

response = requests.get("http://www.funtrivia.com/playquiz/quiz18138014c52e8.html")
print(response.text)