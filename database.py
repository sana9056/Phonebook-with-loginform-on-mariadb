import mariadb
"""
Основной файл для работы c базой данных
!!!Здесь ОБЯЗАТЕЛЬНО прописать данные для подключения к БД!!!
#sana9056
"""
conn = mariadb.connect(
        user = "root",    #<---- Здесь прописываем имя пользователя, которого указывали при установки базы данных
        password = "root",  #<---- Здесь прописываем пароль, если создавали его при установке
        host = "127.0.0.1",  #<---- Здесь прописываем данные хоста для подключения к БД
        port = 3306,     #<---- Здесь прописываем порт подключения к БД
        database = "book"  #<---- !!!Здесь менять ничего не надо!!! это название БД из файла create_db.py
    )
cur = conn.cursor()


def reg_user(name, password, date):
    cur.execute("INSERT INTO users (name, password, date) VALUES (?, ?, ?)", (name, password, date))
    conn.commit()


def add_data(name, phone, date):
    cur.execute("INSERT INTO contacts (name, phone, date) VALUES (?, ?, ?)", (name, phone, date))
    conn.commit()
