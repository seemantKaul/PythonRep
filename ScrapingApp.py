import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, "html.parser")
# print(soup.prettify())

storyList = soup.find_all(name='storylink')
print(storyList)