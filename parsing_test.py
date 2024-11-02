import requests
from bs4 import BeautifulSoup
import json
# URL сайта
url = "https://quotes.toscrape.com"
# Сбор данных
quotes_list = []
while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Извлечение данных
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        
        quotes_list.append({
            "text": text,
            "author": author,
            "tags": tags
        })
    
    # Переход на следующую страницу
    next_button = soup.find('li', class_='next')
    url = f"https://quotes.toscrape.com{next_button.find('a')['href']}" if next_button else None
# Сохранение данных в JSON файл
with open('quotes.json', 'w', encoding='utf-8') as json_file:
    json.dump(quotes_list, json_file, ensure_ascii=False, indent=4)
print("Парсинг завершен. Данные сохранены в quotes.json")