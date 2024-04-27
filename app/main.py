from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/extract-text/")
def extract_text(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    images = [img['src'] for img in soup.find_all('img') if img.has_attr('src')]
    # Extract images from other tags like divs with background images
    style_images = [tag['style'] for tag in soup.find_all(style=True) if 'background-image' in tag['style']]
    return {'text': text, 'images': images + style_images}
