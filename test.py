import sqlite3
import pandas as pd

# Подключение к базе данных
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Создание таблицы Movie
cur.execute('''
    CREATE TABLE IF NOT EXISTS Movie (
        budget REAL,
        runtime REAL,
        score REAL,
        votes REAL,
        gross REAL,
        rating TEXT,
        genre TEXT,
        director TEXT,
        company TEXT,
        writer TEXT,
        star TEXT,
        country TEXT
    );
''')

# Чтение данных из файла movies.csv
movies_df = pd.read_csv('movies.csv')

# Заполнение таблицы Movie данными из файла movies.csv
for index, row in movies_df.iterrows():
    cur.execute('''
        INSERT INTO Movie (budget, runtime, score, votes, gross, rating, genre, director, company, writer, star, country)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    ''', (row['budget'], row['runtime'], row['score'], row['votes'], row['gross'], row['rating'], row['genre'], row['director'], row['company'], row['writer'], row['star'], row['country']))

# Сохранение изменений и закрытие соединения с базой данных
conn.commit()
conn.close()





