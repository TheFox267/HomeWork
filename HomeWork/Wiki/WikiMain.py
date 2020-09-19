import sys
import requests
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import wikipedia
from PIL import Image

lang = 'en'


def search_func():
    wikipedia.set_lang(lang)
    try:
        query = main_window.search_entry.text()
        answer = wikipedia.WikipediaPage(query)
        image = [word for word in filter(lambda x: x.endswith('.jpg', ), answer.images)]
        response = requests.get(image[0], stream=True)
        with open('image.png', 'wb') as image:
            image.write(response.content)
        Image.open('image.png').save('image.png')
        pixmap = QPixmap('image.png')
        main_window.heading_label.setText(answer.title)
        main_window.text_label.setText(answer.summary)
        main_window.image_label.setPixmap(pixmap)

    except:
        QtWidgets.QMessageBox.critical(main_window, 'Ошибка', 'Данной статьи не существует')


def save_doc():
    with open('Wiki article.txt', 'w', encoding='utf-8') as file:
        file.write(main_window.heading_label.text() + '\n' + main_window.text_label.text())
    QtWidgets.QMessageBox.information(main_window, 'Информация', 'Файл сохранён')


def change_on_en_func():
    global lang
    lang = 'en'


def change_on_de_func():
    global lang
    lang = 'de'


def change_on_fr_func():
    global lang
    lang = 'fr'


def change_on_pl_func():
    global lang
    lang = 'pl'


def change_on_ru_func():
    global lang
    lang = 'ru'


app = QtWidgets.QApplication(sys.argv)

main_window = uic.loadUi('Main_Window.ui')

main_window.search_button.clicked.connect(search_func)
main_window.save_button.clicked.connect(save_doc)
main_window.action.triggered.connect(change_on_en_func)
main_window.action_2.triggered.connect(change_on_de_func)
main_window.action_3.triggered.connect(change_on_ru_func)
main_window.action_4.triggered.connect(change_on_pl_func)
main_window.action_5.triggered.connect(change_on_fr_func)

main_window.show()

app.exec_()
