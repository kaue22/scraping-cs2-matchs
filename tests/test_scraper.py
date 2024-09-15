import unittest
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
from datetime import datetime
import locale
from results.scraper import extract_news_titles

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

class TestExtractNewsTitles(unittest.TestCase):
    @patch('requests.get')
    def test_extract_news_titles(self, mock_get):
        html_content = '''
        <div class="matches-group-header">15 de setembro, 2024</div>
        <div class="match-results">
            <a href="/partidas/12345">Partida 1</a>
            <a href="/partidas/67890">Partida 2</a>
        </div>
        '''
    
        mock_response = Mock()
        mock_response.content = html_content
        mock_get.return_value = mock_response
        with patch('builtins.print') as mocked_print:
            extract_news_titles()
            mocked_print.assert_any_call("/partidas/12345")
            mocked_print.assert_any_call("/partidas/67890")

if __name__ == '__main__':
    unittest.main()
