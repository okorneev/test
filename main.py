from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Имя пользователя: "),
        password=getpass("Пароль: "),
    ) as connection:
        print(connection)
except Error as e:
    print(e)
try:
    with  connect(
        host="localhost",
        user=input("Введите имя пользователя: "),
        password=getpass("Введите парhhhоль:"),
    ) as connection:
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
except Error as e:
    print(e)

