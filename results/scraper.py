import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def extract_news_titles():
    formatter = "%d de %B, %Y"
    url = "https://www.dust2.com.br/resultados"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    matches_group_headers = soup.select(".matches-group-header")
    
    for header in matches_group_headers:
        received_date = datetime.strptime(header.text.strip(), formatter).date()
        if received_date == (datetime.now().date()):
            matches_group_containers = soup.select(".match-results")
            
            for container in matches_group_containers:
                if received_date == (datetime.now().date()):
                    for link in container.select("a[href^='/partidas/']"):
                     href = link['href']
                     print(href)
extract_news_titles()
