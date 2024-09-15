import unittest
from unittest.mock import patch, Mock
from results.scraper import extract_news_titles
from bs4 import BeautifulSoup

class TestExtractNewsTitles(unittest.TestCase):

    @patch('requests.get')
    def test_extract_news_titles(self, mock_get):
        # Mockando a resposta do requests.get
        mock_response = Mock()
        mock_response.content = '''
        <html>
            <div class="matches-group-header">14 de setembro, 2024</div>
            <div class="match-results">
                <a href="/partidas/123">Match 1</a>
                <a href="/partidas/456">Match 2</a>
            </div>
        </html>
        '''
        mock_get.return_value = mock_response

        with patch('builtins.print') as mocked_print:
            extract_news_titles()
            mocked_print.assert_any_call('/partidas/123')
            mocked_print.assert_any_call('/partidas/456')

if __name__ == '__main__':
    unittest.main()