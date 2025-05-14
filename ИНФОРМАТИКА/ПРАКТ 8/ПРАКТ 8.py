# ===========================
# Практическая работа №8
# ===========================

import pandas as pd

# 1. Чтение файла. Функция read_csv()
# Указываем разделитель (запятая), при необходимости — кодировку
df = pd.read_csv('sample.csv', delimiter=',', encoding='utf-8')
print("Первичные данные:\n", df)

# 2. columns()
print("Названия столбцов:", df.columns.tolist())

# 3. Очистка данных. Валидность данных
# Проверка на пропуски
print("Количество пропущенных значений:\n", df.isnull().sum())

# Заполнение пропусков или удаление
# Например, удалим строки с пропущенными значениями
df_clean = df.dropna()
print("Данные после удаления пропусков:\n", df_clean)

# 4. unique() и info()
# Получим уникальные значения в столбце 'Profession'
if 'Profession' in df_clean.columns:
    print("Уникальные профессии:\n", df_clean['Profession'].unique())

# Общая информация о DataFrame
df_clean.info()

# 5. Перечислите ошибки в данных
# Возможные ошибки:
# - Пустые значения в ключевых столбцах ('Name', 'City')
# - Дублирующиеся строки
# - Неверный регистр/формат данных (например, 'Name' в разном регистре)
# Для этого можно выполнить проверку:
print("Дублирующиеся строки:\n", df_clean[df_clean.duplicated()])

# 6. Удаление столбца. drop()
# Например, удалим столбец 'City', если он не нужен
if 'City' in df_clean.columns:
    df_clean = df_clean.drop(columns=['City'])
    print("Данные после удаления 'City':\n", df_clean)

# 7. Фильтрация ошибок. query()
# Например, выбрать всех возрастом выше 30
# Перед этим убедимся, что 'Age' — числовой тип
df_clean['Age'] = pd.to_numeric(df_clean['Age'], errors='coerce')
filtered_df = df_clean.query('Age > 30')
print("Люди старше 30:\n", filtered_df)

# 8. str.match() и str.contains()
# Проверка имени на определённый паттерн
if 'Name' in df_clean.columns:
    # Имена, начинающиеся на 'И'
    mask_starting_И = df_clean['Name'].str.match(r'^И', na=False)
    print("Имёна, начинающиеся на 'И':\n", df_clean[mask_starting_И])

    # Имена, содержащие 'ов'
    mask_contains_ов = df_clean['Name'].str.contains(r'ов', na=False)
    print("Имёна, содержащие 'ов':\n", df_clean[mask_contains_ов])

# 9. apply()
# Например, создадим новый столбец, где возраст увеличен на 10%
if 'Age' in df_clean.columns:
    df_clean['Age_plus_10'] = df_clean['Age'].apply(lambda x: x * 1.1 if pd.notnull(x) else x)
    print("Возраст с добавленным 10%:\n", df_clean[['Age', 'Age_plus_10']])

# 10. Общий алгоритм анализа:
# - Загрузка данных (уже сделана)
# - Проверка и очистка (пропуски, дубли)
# - Анализ распределения (например, по возрасту)
# - Группировка по профессии
if 'Profession' in df_clean.columns:
    group_counts = df_clean.groupby('Profession').size()
    print("Количество по профессиям:\n", group_counts)

# Итог
# Можно сохранять обработанные данные
# df_clean.to_csv('sample_cleaned.csv', index=False)



#===========================================================================================
#===========================================================================================
#===========================================================================================

print("")
print("ПРАКТИЧЕСКАЯ №(8)")

import pandas as pd
from datetime import datetime

films_df = pd.read_csv('films.csv')

# Преобразование столбца release_date в формат даты
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%m/%d/%Y')
    except:
        return pd.NaT

films_df['release_date_parsed'] = films_df['release_date'].apply(parse_date)

# Определение функции, является ли дата зимой
def is_winter(date):
    if pd.isnull(date):
        return False
    return date.month in [12, 1, 2]

# Создаем колонку, указывающую, зимой ли вышел фильм
films_df['is_winter'] = films_df['release_date_parsed'].apply(is_winter)

# Отфильтруем фильмы, выпущенные зимой
winter_films = films_df[films_df['is_winter']]

# Подсчет количества фильмов по режиссерам
director_counts = winter_films['director'].value_counts()

# Находим режиссера с максимальным количеством фильмов зимой
top_director = director_counts.idxmax()
top_films_count = director_counts.max()

print(f"Режиссер, который выпускает больше всего фильмов зимой: {top_director} ({top_films_count} фильмов)")