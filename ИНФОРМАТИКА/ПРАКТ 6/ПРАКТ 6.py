# ===========================
# Практическая работа №6
# ===========================

import pandas as pd
from IPython.display import display

# Библиотека Pandas. Импорт библиотеки
# (уже выполнено выше)

# Структура Series. Примеры
s1 = pd.Series([10, 20, 30, 40])  # Создание Series из списка
s2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])  # Series с пользовательскими индексами

# Создание Series. Примеры
display(s1)
display(s2)

# Доступ к элементам Series с использованием .loc или .iloc
print("Элемент с индексом 'b':", s2.loc['b'])
print("Первый элемент Series s2:", s2.iloc[0])

# Объект DataFrame. Создание. Синтаксис. Примеры
data = {
    'Имя': ['Андрей', 'Мария', 'Иван'],
    'Возраст': [25, 30, 22],
    'Город': ['Москва', 'Санкт-Петербург', 'Казань']
}
df = pd.DataFrame(data)
display(df)

# Функция read_csv. Синтаксис. Примеры
df_football = pd.read_csv('football.csv')

# Получение информации о датафрейме: head и tail
print("Первые 5 строк:\n", df_football.head())
print("Последние 5 строк:\n", df_football.tail())

# Получение информации о датафрейме: info
df_football.info()

# Получение информации о датафрейме: describe
print("Статистические показатели по числовым столбцам:\n", df_football.describe())

# Индексация и извлечение данных: статистические методы
# Среднее по столбцу 'Goals'
if 'Goals' in df_football.columns:
    mean_goals = df_football['Goals'].mean()
    print("Среднее количество голов:", mean_goals)

# Максимальный возраст
if 'Age' in df_football.columns:
    max_age = df_football['Age'].max()
    print("Максимальный возраст:", max_age)


#===========================================================================================
#===========================================================================================
#===========================================================================================


print("")
print("ПРАКТИЧЕСКАЯ №(6)")

import pandas as pd

df = pd.read_csv("football.csv")

df['Wage'] = df['Wage'].replace({',': ''}, regex=True).astype(int)
df['SprintSpeed'] = pd.to_numeric(df['SprintSpeed'], errors='coerce')

average_wage = df['Wage'].mean()

high_wage_players = df[df['Wage'] > average_wage]

average_speed = high_wage_players['SprintSpeed'].mean()

result = round(average_speed, 2)

print("Средняя скорость футболистов с зарплатой выше среднего:", result)