from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch
from requests.models import Response

client = TestClient(app)

def test_extract_text():
    mock_response = Response()
    mock_response.status_code = 200
    mock_response._content = b'<html><body>Hello World<img src="http://example.com/image.png"></body></html>'
    with patch('requests.get', return_value=mock_response):
        response = client.get("/extract-text/", params={'url': 'http://example.com'})
        assert response.status_code == 200
        assert response.json() == {'text': 'Hello World', 'images': ['http://example.com/image.png']}
