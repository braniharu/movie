import sqlite3
import pandas as pd

# Считываем датасет
movies_df = pd.read_csv('movies.csv')

# Создаем базу данных
conn = sqlite3.connect('movies.db')

# Создаем таблицу Rating
conn.execute('''CREATE TABLE Rating
                (rating TEXT PRIMARY KEY)''')

# Заполняем таблицу Rating уникальными значениями из столбца 'rating' датасета
rating_values = movies_df['rating'].unique()
for rating in rating_values:
    conn.execute("INSERT INTO Rating (rating) VALUES (?)", (rating,))

# Аналогично создаем и заполняем таблицы Genre, Company, Country, Director, Star и Writer
conn.execute('''CREATE TABLE Genre
                (genre TEXT PRIMARY KEY)''')
genre_values = movies_df['genre'].unique()
for genre in genre_values:
    conn.execute("INSERT INTO Genre (genre) VALUES (?)", (genre,))

conn.execute('''CREATE TABLE Company
                (company TEXT PRIMARY KEY)''')
company_values= movies_df['company'].unique()
for company in company_values:
    conn.execute("INSERT INTO Company (company) VALUES (?)", (company,))

conn.execute('''CREATE TABLE Country
                (country TEXT PRIMARY KEY)''')
country_values = movies_df['country'].unique()
for country in country_values:
    conn.execute("INSERT INTO Country (country) VALUES (?)", (country,))

conn.execute('''CREATE TABLE Director
                (director TEXT PRIMARY KEY)''')
director_values = movies_df['director'].unique()
for director in director_values:
    conn.execute("INSERT INTO Director (director) VALUES (?)", (director,))

conn.execute('''CREATE TABLE Star
                (star TEXT PRIMARY KEY)''')
star_values = movies_df['star'].unique()
for star in star_values:
    conn.execute("INSERT INTO Star (star) VALUES (?)", (star,))

conn.execute('''CREATE TABLE Writer
                (writer TEXT PRIMARY KEY)''')
writer_values = movies_df['writer'].unique()
for writer in writer_values:
    conn.execute("INSERT INTO Writer (writer) VALUES (?)", (writer,))

# Создаем таблицу Film
conn.execute('''CREATE TABLE Film
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 rating TEXT,
                 genre TEXT,
                 company TEXT,
                 country TEXT,
                 director TEXT,
                 star TEXT,
                 writer TEXT,
                 budget REAL,
                 gross REAL,
                 year REAL,
                 rating REAL)''')

# Заполняем таблицу Film значениями из датасета
for index, row in movies_df.iterrows():
    rating = row['rating']
    genre = row['genre']
    company = row['company']
    country = row['country']
    director = row['director']
    star = row['star']
    writer = row['writer']
    budget = row['budget']
    gross = row['gross']
    year = row['year']
    rating = row['rating']
    
    # Получаем id из таблиц Rating, Genre, Company, Country, Director, Star и Writer
    rating_id = conn.execute("SELECT rowid FROM Rating WHERE rating=?", (rating,)).fetchone()[0]
    genre_id = conn.execute("SELECT rowid FROM Genre WHERE genre=?", (genre,)).fetchone()[0]
    company_id = conn.execute("SELECT rowid FROM Company WHERE company=?", (company,)).fetchone()[0]
    country_id = conn.execute("SELECT rowid FROM Country WHERE country=?", (country,)).fetchone()[0]
    director_id = conn.execute("SELECT rowid FROM Director WHERE director=?", (director,)).fetchone()[0]
    star_id = conn.execute("SELECT rowid FROM Star WHERE star=?", (star,)).fetchone()[0]
    writer_id = conn.execute("SELECT rowid FROM Writer WHERE writer=?", (writer,)).fetchone()[0]
    
    # Вставляем данные в таблицу Film
    conn.execute("INSERT INTO Film (rating, genre, company, country, director, star, writer, budget, gross, year, rating) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (rating_id, genre_id, company_id, country_id, director_id, star_id, writer_id, budget, gross, year, rating))

# Сохраняем изменения в базе данных
conn.commit()