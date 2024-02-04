import tkinter as tk
from tkinter import ttk
import numpy as np
from model import is_profitable, RATING, GENRE, COMPANY, DIRECTOR, WRITER, STAR, COUNTRY, movies_df

def predict_profitability():
    budget = float(budget_entry.get())
    runtime = float(runtime_entry.get())
    score = float(score_entry.get())
    votes = float(votes_entry.get())
    rating = rating_dropdown.get()
    genre = genre_dropdown.get()
    director = director_dropdown.get()
    company = company_dropdown.get()
    writer = writer_dropdown.get()
    star = star_dropdown.get()
    country = country_dropdown.get()

    # приводим категориальные признаки к индексам
    rating_codes = np.where(RATING == rating)[0][0] 
    genre_codes = np.where(GENRE == genre)[0][0] 
    director_codes = np.where(DIRECTOR == director)[0][0] 
    company_codes = np.where(COMPANY == company)[0][0] 
    writer_codes = np.where(WRITER == writer)[0][0]
    star_codes = np.where(STAR == star)[0][0]
    country_codes = np.where(COUNTRY == country)[0][0]
    rating_codes = int(rating_codes)
    genre_codes = int(genre_codes)
    director_codes = int(director_codes)
    company_codes = int(company_codes)
    writer_codes = int(writer_codes)
    star_codes = int(star_codes)
    country_codes = int(country_codes)

    # передаем целочисленные коды в функцию модели
    profitability = is_profitable(budget, runtime, score, votes, rating_codes, genre_codes, director_codes, 
                                  company_codes, writer_codes, star_codes, country_codes, movies_df)
    
    result_label.config(text=f"Окупаемость: {profitability}")


# Создаем главное окно
window = tk.Tk()
window.title("Прогнозирование окупаемости фильма")
window.geometry('400x550')

# Создаем текстовые метки и поля для ввода значений
budget_label = ttk.Label(window, text="Бюджет: ")
budget_entry = ttk.Entry(window)

runtime_label = ttk.Label(window, text="Продолжительность: ")
runtime_entry = ttk.Entry(window)

score_label = ttk.Label(window, text="Рейтинг: ")
score_entry = ttk.Entry(window)

votes_label = ttk.Label(window, text="Количество голосовавших: ")
votes_entry = ttk.Entry(window)

rating_label = ttk.Label(window, text="Возрастное ограничение: ")
rating_dropdown = ttk.Combobox(window, values=list(RATING))

genre_label = ttk.Label(window, text="Жанр: ")
genre_dropdown = ttk.Combobox(window, values=list(GENRE))

director_label = ttk.Label(window, text="Режиссёр: ")
director_dropdown = ttk.Combobox(window, values=list(DIRECTOR))

company_label = ttk.Label(window, text="Компания: ")
company_dropdown = ttk.Combobox(window, values=list(COMPANY))

writer_label = ttk.Label(window, text="Сценарист: ")
writer_dropdown = ttk.Combobox(window, values=list(WRITER))

star_label = ttk.Label(window, text="Популярный актёр: ")
star_dropdown = ttk.Combobox(window, values=list(STAR))

country_label = ttk.Label(window, text="Страна-производитель: ")
country_dropdown = ttk.Combobox(window, values=list(COUNTRY))

# Создаем кнопку для прогнозирования окупаемости
predict_button = ttk.Button(window, text="Прогнозировать окупаемость", command=predict_profitability)

# Отображаем все элементы на экране
budget_label.pack()
budget_entry.pack()

runtime_label.pack()
runtime_entry.pack()

score_label.pack()
score_entry.pack()

votes_label.pack()
votes_entry.pack()

rating_label.pack()
rating_dropdown.pack()

genre_label.pack()
genre_dropdown.pack()

director_label.pack()
director_dropdown.pack()

company_label.pack()
company_dropdown.pack()

writer_label.pack()
writer_dropdown.pack()

star_label.pack()
star_dropdown.pack()

country_label.pack()
country_dropdown.pack()

predict_button.pack()

result_label = ttk.Label(window, text="Окупаемость =")
result_label.pack()

window.mainloop()
    