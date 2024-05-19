import psycopg2
from faker import Faker
import random
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

    fake = Faker()

    with connection.cursor() as cursor:
        # Заполнение Users
        for i in range(50):
            first_name = fake.first_name()
            second_name = fake.last_name()
            phone = (fake.country_calling_code() + fake.unique.msisdn())[:19]
            email = fake.unique.ascii_company_email()
            cursor.execute("insert into Users (first_name, second_name, phone, email) values (%s, %s, %s, %s)",
                           (first_name, second_name, phone, email))
        for i in range(50):
            first_name = fake.first_name()
            phone = (fake.country_calling_code() + fake.unique.msisdn())[:19]
            email = fake.unique.ascii_company_email()
            cursor.execute("insert into Users (first_name, phone, email) values (%s, %s, %s)",
                           (first_name, phone, email))

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
