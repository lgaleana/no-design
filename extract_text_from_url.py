import requests
from bs4 import BeautifulSoup


def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    print(text)
    return text

