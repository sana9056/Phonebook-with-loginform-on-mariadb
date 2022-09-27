import mariadb

"""
Скрипт создания Базы данных. Запустить перед запусом приложения. !!!Один раз!!!
!!!Здесь ОБЯЗАТЕЛЬНО прописать данные для подключения к БД перед запуском скрипта!!!
#sana9056
"""


class create_db():
    conn = mariadb.connect(
        user = "root", #<---- Здесь прописываем имя пользователя, которого указывали при установки базы данных
        password="root", #<---- Здесь прописываем пароль, если создавали его при установке
        host = "127.0.0.1", #<---- Здесь прописываем данные хоста для подключения к БД
    )
    cur = conn.cursor()

    cur.execute("CREATE DATABASE book;")
    conn.commit()

    conn = mariadb.connect(
        user = "root",  #<---- Здесь прописываем имя пользователя, которого указывали при установки базы данных
        password="root",  #<---- Здесь прописываем пароль, если создавали его при установке
        host = "127.0.0.1",  #<---- Здесь прописываем данные хоста для подключения к БД
        database='book'
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE users ("
                "id INT AUTO_INCREMENT, "
                "name VARCHAR (100), "
                "password VARCHAR (100), "
                "date DATE, "
                "remember_me INT, "
                "PRIMARY KEY (id))")
    conn.commit()
    cur.execute("CREATE TABLE contacts ("
                "id INT AUTO_INCREMENT, "
                "name VARCHAR (100), "
                "phone VARCHAR (100), "
                "date DATE, "
                "PRIMARY KEY (id))")
    conn.commit()
    print('Database is created')
    input()


if __name__ == '__main__':
    create_db()
