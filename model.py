import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('database.db')

# Считываем датасет
movies_df = pd.read_sql_query("SELECT * FROM Movie", conn)

# Оставляем только необходимые для обучения признаки
#movies_df.drop(['name', 'year', 'released'], axis=1, inplace=True)

#Удаление пропущенных значений
movies_df.dropna(how='any', inplace=True)

RATING = movies_df.rating.unique()
GENRE = movies_df.genre.unique()
COMPANY = movies_df.company.unique()
DIRECTOR = movies_df.director.unique()
WRITER = movies_df.writer.unique()
STAR = movies_df.star.unique()
COUNTRY = movies_df.country.unique()

def is_profitable(budget, runtime, score, votes, rating_codes, genre_codes, director_codes, 
                                  company_codes, writer_codes, star_codes, country_codes, movies_df):

    # Преобразуем категориальные признаки в числовые
    rating_codes = pd.factorize(movies_df['rating'])[0]
    genre_codes = pd.factorize(movies_df['genre'])[0]
    company_codes = pd.factorize(movies_df['company'])[0]
    director_codes = pd.factorize(movies_df['director'])[0]
    writer_codes = pd.factorize(movies_df['writer'])[0]
    star_codes = pd.factorize(movies_df['star'])[0]
    country_codes = pd.factorize(movies_df['country'])[0]   
    
    movies_df['rating'] = rating_codes
    movies_df['genre'] = genre_codes
    movies_df['company'] = company_codes
    movies_df['director'] = director_codes
    movies_df['writer'] = writer_codes
    movies_df['star'] = star_codes
    movies_df['country'] = country_codes

    # Разделяем данные на тренировочный и тестовый наборы
    X_train, X_test, y_train, y_test = train_test_split(movies_df.drop('gross', axis=1), (movies_df['gross'] > movies_df['budget']), test_size=0.2, random_state=42)
    
    # Обучаем модель методом случайного леса
    model = RandomForestClassifier()
    model.fit(X_train.values, y_train)
    accuracy = model.score(X_test.values, y_test)
    print("Точность модели = ", accuracy)

    is_profitable = model.predict([[budget, runtime, score, votes, 
                                    rating_codes[0], genre_codes[0], director_codes[0], company_codes[0],
                                    writer_codes[0], star_codes[0], country_codes[0]]])
    
    predicted_gross = model.predict([[budget, runtime, score, votes, 
                                rating_codes[0], genre_codes[0], director_codes[0], company_codes[0],
                                writer_codes[0], star_codes[0], country_codes[0]]])
    print(predicted_gross)
    return bool(is_profitable)