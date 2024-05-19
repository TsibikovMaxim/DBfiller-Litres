host = "localhost"
user = "postgres"
password = "1111"
db_name = "postgres"

#    # Заполнение Users
#    for i in range(50):
#        first_name = fake.first_name()
#        second_name = fake.last_name()
#        phone = (fake.country_calling_code() + fake.unique.msisdn())[:19]
#        email = fake.unique.ascii_company_email()
#        cursor.execute("insert into Users (first_name, second_name, phone, email) values (%s, %s, %s, %s)",
#                       (first_name, second_name, phone, email))
#    for i in range(50):
#        first_name = fake.first_name()
#        phone = (fake.country_calling_code() + fake.unique.msisdn())[:19]
#        email = fake.unique.ascii_company_email()
#        cursor.execute("insert into Users (first_name, phone, email) values (%s, %s, %s)",
#                       (first_name, phone, email))
#
#    # Заполнение SubscriptionTypes
#    for i in range(20):
#        name = fake.unique.word()
#        duration = f'P{random.randint(0, 3)}Y{random.randint(1, 12)}M{random.randint(1, 30)}DT0H0M0S'
#        description = fake.text()
#        price = random.randint(100, 99999) / 100
#        cursor.execute("insert into SubscriptionTypes (name, duration, description, price)"
#                       " values (%s, %s, %s, %s)",
#                       (name, duration, description, price))
#
#    # Заполняем UsersSubscriptions
#    for i in range(1, 114):
#        if (random.randint(2, 6) % 3 == 0):
#            for j in range(1, 30):
#                if (random.randint(2, 6) % 3 == 0):
#                    start_date = str(fake.date_between(start_date='-5y'))
#                    cursor.execute("insert into UsersSubscriptions (user_id, sub_type_id, start_date)" "values ("
#                                   "%s, %s, %s)",
#                                   (i, j, start_date))
#
#    # Заполняем ReadbleBooks
#    for i in range(50):
#        page_count = random.randint(100, 10000)
#        publication_date = str(fake.date_between(start_date='-5y'))
#        price = random.randint(100, 99999) / 100
#        cursor.execute(
#            "insert into ReadbleBooks (page_count, publication_date, product_type, price)" "values (%s, %s, %s, "
#            "%s)",
#            (page_count, publication_date, 'P', price))
#    for i in range(50):
#        page_count = random.randint(100, 10000)
#        publication_date = str(fake.date_between(start_date='-5y'))
#        cursor.execute("insert into ReadbleBooks (page_count, publication_date, product_type)"
#                       " values (%s, %s, %s)",
#                       (page_count, publication_date, 'F'))
#
#    # Заполняем Studios
#    for i in range(20):
#        name = fake.unique.name()
#        description = fake.text()
#        cursor.execute(
#            "insert into Studios (name, description) values (%s, %s)", (name, description))
#
#    # Заполняем AudioBooks
#    for i in range(25):
#        duration = fake.time()
#        publication_date = str(fake.date_between(start_date='-5y'))
#        price = random.randint(100, 99999) / 100
#        studio_id = random.randint(100, 200) % 20 + 1
#        cursor.execute(
#            "insert into AudioBooks (duration, publication_date, product_type, price, studio_id)" " values (%s, %s, %s, %s, %s)",
#            (duration, publication_date, 'P', price, studio_id))
#    for i in range(25):
#        duration = fake.time()
#        publication_date = str(fake.date_between(start_date='-5y'))
#        studio_id = random.randint(100, 200) % 20 + 1
#        cursor.execute(
#            "insert into AudioBooks (duration, publication_date, product_type, studio_id)"
#            " values (%s, %s, %s, %s)",
#            (duration, publication_date, 'F', studio_id))
#
#    # Заполняем Voiceover
#    for i in range(40):
#        name = fake.unique.name()
#        description = fake.text()
#        cursor.execute(
#            "insert into Voiceover (name, biography) values (%s, %s)", (name, description))
#
#    # Заполняем AudioVoiceover
#    for i in range(1, 51):
#        if random.randint(2, 6) % 3 == 0:
#            for j in range(random.randint(1, 6)):
#                cursor.execute("insert into AudioVoiceover (audio_id, voicer_id) values (%s, %s)",
#                               (i, random.randint(1, 40)))
#        else:
#            cursor.execute("insert into AudioVoiceover (audio_id, voicer_id) values (%s, %s)",
#                           (i, random.randint(1, 40)))
#
#    # Заполняем BookTable
#    SETaudio_ids = [i for i in range(1, 51)]
#    SETreadble_ids = [i for i in range(1, 108)]
#    for i in range(30):
#        name = fake.unique.word()
#        image_path = fake.file_path(depth=5, extension='png')
#        synopsis = fake.text()
#        audio_id = random.choice(SETaudio_ids)
#        SETaudio_ids.remove(audio_id)
#        readble_id = random.choice(SETreadble_ids)
#        SETreadble_ids.remove(readble_id)
#        cursor.execute("insert into BookTable (name, image_path, synopsis, audio_id, readble_id)"
#                       " values (%s, %s, %s, %s, %s)",
#                       (name, image_path, synopsis, audio_id, readble_id))
#
#    for i in range(20):
#        name = fake.unique.word()
#        image_path = fake.file_path(depth=5, extension='png')
#        synopsis = fake.text()
#        audio_id = random.choice(SETaudio_ids)
#        SETaudio_ids.remove(audio_id)
#        cursor.execute(
#            "insert into BookTable (name, image_path, synopsis, audio_id) values (%s, %s, %s, %s)",
#            (name, image_path, synopsis, audio_id))
#
#    for i in range(77):
#        name = fake.unique.word()
#        image_path = fake.file_path(depth=5, extension='png')
#        synopsis = fake.text()
#        readble_id = random.choice(SETreadble_ids)
#        SETreadble_ids.remove(readble_id)
#        cursor.execute(
#            "insert into BookTable (name, image_path, synopsis, readble_id) values (%s, %s, %s, %s)",
#            (name, image_path, synopsis, readble_id))
#
#
#    def getOrr():
#        if (random.randint(2, 7) % 2 == 0):
#            return "a"
#        else:
#            return "r"
#
#
#    # Заполняем BooksUsers
#    for i in range(1, 113):
#        if (random.randint(2, 7) % 3 == 0):
#            for j in range(random.randint(1, 7)):
#                cursor.execute("insert into BooksUsers (book_id, user_id, book_type) values (%s, %s, %s)",
#                               (random.randint(1, 127), i, getOrr()))
#        else:
#            cursor.execute("insert into BooksUsers (book_id, user_id, book_type) values (%s, %s, %s)",
#                           (random.randint(1, 127), i, getOrr()))
#
#    # Заполняем Categories
#    for i in range(20):
#        name = fake.unique.word()
#        description = fake.text()
#        cursor.execute(
#            "insert into Categories (name, description) values (%s, %s)", (name, description))
#
#    # Заполняем BooksCategories
#    for i in range(1, 128):
#        if (random.randint(2, 7) % 3 == 0):
#            for j in range(random.randint(1, 7)):
#                cursor.execute("insert into BooksCategories (book_id, categ_id) values (%s, %s)",
#                               (i, random.randint(1, 20)))
#        else:
#            cursor.execute("insert into BooksCategories (book_id, categ_id) values (%s, %s)",
#                           (i, random.randint(1, 20)))
#
#    # Заполняем Authors
#    for i in range(80):
#        name = fake.unique.name()
#        description = fake.text()
#        cursor.execute(
#            "insert into Authors (name, biography) values (%s, %s)", (name, description))
#
#    # Заполняем BooksAuthors
#    for i in range(1, 128):
#        if (random.randint(2, 6) % 3 == 0):
#            for j in range(random.randint(1, 5)):
#                cursor.execute("insert into BooksAuthors (book_id, author_id) values (%s, %s)",
#                               (i, random.randint(1, 80)))
#        else:
#            cursor.execute("insert into BooksAuthors (book_id, author_id) values (%s, %s)",
#                           (i, random.randint(1, 80)))
#
#    # Заполняем Transactions
#    SETcods = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#               1, -1, -100, -102, 5, 15, 53, 100]
#    for i in range(20):
#        user_id = random.randint(1, 113)
#        audiobook_id = random.randint(1, 25)
#        date = str(fake.date_between(start_date='-5y'))
#        checking_account = fake.isbn13()
#        trans_status = random.choice(SETcods)
#        cursor.execute(
#            "insert into Transactions (user_id, audiobook_id, date, checking_account, "
#            "trans_status, price) values( % s, % s, % s, % s, % s, % s)",
#            (user_id, audiobook_id, date, checking_account, trans_status, 0))
#
#    for i in range(25):
#        user_id = random.randint(1, 113)
#        readblebook_id = random.randint(5, 57)
#        date = str(fake.date_between(start_date='-5y'))
#        checking_account = fake.isbn13()
#        trans_status = random.choice(SETcods)
#        cursor.execute(
#            "insert into Transactions (user_id, readblebook_id, date, checking_account, "
#            "trans_status, price) values( % s, % s, % s, % s, % s, % s)",
#            (user_id, readblebook_id, date, checking_account, trans_status, 0))
#
#    for i in range(15):
#        user_id = random.randint(1, 113)
#        subscription_id = random.randint(1, 29)
#        date = str(fake.date_between(start_date='-5y'))
#        checking_account = fake.isbn13()
#        trans_status = random.choice(SETcods)
#        cursor.execute(
#            "insert into Transactions (user_id, subscription_id, date,# checking_account, "
#            "trans_status, price) values( % s, % s, % s, % s, % s, % s)",
#            (user_id, subscription_id, date, checking_account, trans_status, 0))