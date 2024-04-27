import pytest
from unittest.mock import patch
from extract_text_from_url import extract_text

@patch('requests.get')
def test_extract_text(mock_get):
    mock_get.return_value.content = b'<html><body>Hello World</body></html>'
    assert extract_text('http://example.com') == 'Hello World'
