import psycopg2
import random
import pandas as pd
from config import host, user, password, db_name

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        excel_file = 'users.xlsx'
        df = pd.read_excel(excel_file)

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            second_name TEXT,
            phone TEXT,
            email TEXT
        )
        ''')

        def insert_user(first_name, second_name, phone, email):
            cursor.execute('''
            INSERT INTO Users (first_name, second_name, phone, email)
            VALUES (?, ?, ?, ?)
            ''', (first_name, second_name, phone, email))
            connection.commit()


        for index, row in df.iterrows():
            insert_user(row['first_name'], row['second_name'], row['phone'], row['email'])

        connection.close()

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
