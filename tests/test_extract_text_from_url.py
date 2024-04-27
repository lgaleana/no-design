import pytest
from unittest.mock import patch
from extract_text_from_url import extract_text

def test_extract_text():
    with patch('requests.get') as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.content = b'<html><body>Hello, world!</body></html>'
        result = extract_text('http://example.com')
        assert result == 'Hello, world!'
