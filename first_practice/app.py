import datetime
import os
from datetime import timedelta
import random
from random import choice
import re

from flask import Flask

app = Flask(__name__)


@app.route('/test')
def test_function():
    now = datetime.datetime.now().utcnow()
    return f'Это тестовая страничка, ответ сгенерирован в {now}'


@app.route('/Hello_world')
def hello_world():
    return 'Привет, мир'


@app.route('/cars')
def cars():
    global cars_list
    cars_list = ['Chevrolet, Renault, Ford, Lada.']
    return cars_list


@app.route('/cats')
def cats():
    cats_list = choice(['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин'])
    return cats_list


@app.route('/get_time/now')
def time():
    now = datetime.datetime.now().utcnow()
    return f'Точное время: {now}'


@app.route('/get_time/future')
def time_future():
    current_time_after_hour = datetime.timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}'


words = []


def get_word():
    if not words:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt.html')
        WORD_PATTERN = r'\b\w+\b'

        with open(BOOK_FILE) as book:
            book_words = re.findall(WORD_PATTERN, book.read())
            words.extend(book_words)
    return words


@app.route('/get_random_word')
def random_word():
    return random.choice(get_word())


x = 0


@app.route('/counter')
def counter():
    global x
    x += 1
    string = (f'Кол-во посещений сайта: {x}')
    return string


if __name__ == '__main__':
    app.run()
