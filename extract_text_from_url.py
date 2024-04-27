import requests
from bs4 import BeautifulSoup

def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()

def main(url):
    text = extract_text(url)
    print(text)

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
