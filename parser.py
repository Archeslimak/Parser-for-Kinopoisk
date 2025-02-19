import requests
from bs4 import BeautifulSoup
import json

def kinopoisk(id):
    page_num = 1
    Data = []

    while True:
        url = f'https://www.kinopoisk.ru/user/{id}/votes/list/vs/vote/page/{page_num}/#list'

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            films = soup.find_all('div', class_='item')
            if len(films) == 0:  # Признак остановки
                break

            for film in films:
                title = film.find('div', class_='nameRus').text.strip()
                Session = film.find('div', class_='date').text.strip()
                rating = film.find('div', class_='vote').text.strip()
                Data.append({'Name': title, 'Data': Session, 'Rating': rating})
            page_num += 1

    return Data

id = input('Введите id: ')
try:
    Data = kinopoisk(id)
    print(Data)
except:
    print("Ошибка!!!")

with open("result.json", "w", encoding='utf-8') as file:
    json.dump(Data, file, ensure_ascii=False)