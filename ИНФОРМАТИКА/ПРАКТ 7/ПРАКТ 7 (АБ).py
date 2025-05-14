# ===========================
# Практическая работа №7
# ===========================


import pandas as pd
import re

# 1. Определение функции. Структура. Аргументы функции. Пример
def calculate_average_scores(df, subject):
    """
    Функция для вычисления среднего балла по указанному предмету.
    Args:
        df (DataFrame): датафрейм с данными
        subject (str): название столбца предмета ('math score', 'reading score', 'writing score')
    Returns:
        float: средний балл
    """
    return df[subject].mean()

# Вызов функции. Примеры
# average_math = calculate_average_scores(df, 'math score')
# print("Средний балл по математике:", average_math)

# 2. Функция как объект. Синтаксис. Примеры
# Можно присвоить функцию переменной
def say_hello(name):
    return f"Привет, {name}!"

greeting = say_hello
print(greeting("Андрей"))  # вызов функции через переменную

# 3. Функция map(). Синтаксис. Пример
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print("Квадраты чисел:", squared)

# 4. Лямбда-функции. Пример
# Создадим функцию, которая возвращает удвоенное значение
double = lambda x: x * 2
print("Удвоенное число 5:", double(5))

# 5. Функция filter(). Пример
# Отфильтруем числа больше 2
filtered_numbers = list(filter(lambda x: x > 2, numbers))
print("Числа больше 2:", filtered_numbers)

# 6. Строка - итерируемый объект. Индексация элементов строки. Синтаксис. Примеры
sample_str = "Hello, World!"
print("Первый символ:", sample_str[0])
print("Последний символ:", sample_str[-1])

# 7. Поиск подстроки в строке. Срез. Синтаксис. Примеры
substring = sample_str[0:5]  # с 0 по 4 индекс
print("Срез строки [0:5]:", substring)

# 8. Метод find(). Синтаксис. Примеры
index = sample_str.find("World")
print("Индекс подстроки 'World':", index)

# 9. Метод count(). Синтаксис. Примеры
count_l = sample_str.count('l')
print("Количество букв 'l':", count_l)

# 10. Методы lower() и upper(). Синтаксис. Примеры
print("В нижнем регистре:", sample_str.lower())
print("В верхнем регистре:", sample_str.upper())

# 11. Метод replace(). Синтаксис. Примеры
replaced_str = sample_str.replace("Hello", "Hi")
print("После замены:", replaced_str)

# 12. Регулярные выражения. Модуль re. Синтаксис. Примеры
text = "Контакт: +7-999-999-99-99"
# Найти телефонный номер
match = re.search(r"\+7-\d{3}-\d{3}-\d{2}-\d{2}", text)
if match:
    print("Обнаружен телефон:", match.group())

# 13. Файл csv. csv- это?
# CSV (Comma Separated Values) — файл, где данные разделены запятыми или другим разделителем.
# Обычно используется для хранения табличных данных.

# 14. Алгоритм анализа данных индивидуального задания
# Общий подход:
# - Загрузка данных
# - Предварительная обработка (очистка, преобразование типов)
# - Анализ данных (статистика, визуализация)
# - Формулировка выводов и рекомендаций

# Загрузка данных из файла 'StudentsPerformance.csv'
df_students = pd.read_csv('StudentsPerformance.csv')

# Демонстрация функций по анализу
# Средние оценки по предметам
avg_math = calculate_average_scores(df_students, 'math score')
avg_reading = calculate_average_scores(df_students, 'reading score')
avg_writing = calculate_average_scores(df_students, 'writing score')

print("Средний балл по математике:", avg_math)
print("Средний балл по чтению:", avg_reading)
print("Средний балл по письму:", avg_writing)

# Получение базовой информации
print(df_students.head())
print(df_students.info())
print(df_students.describe())

# Пример фильтрации: студенты с оценками выше 80
high_scores = df_students[(df_students['math score'] > 80) & 
                            (df_students['reading score'] > 80)]
print("Студенты с высокими оценками:\n", high_scores)



#===========================================================================================
#===========================================================================================
#===========================================================================================



print("")
print("ПРАКТИЧЕСКАЯ №7(А)")

import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

df['writing score'] = pd.to_numeric(df['writing score'], errors='coerce')

count_abiturients = df[df['writing score'] > 90].shape[0]

print("Количество абитуриентов с writing score выше 90:", count_abiturients)



print("")
print("ПРАКТИЧЕСКАЯ №7(Б)")

import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

def find_substring_if_h_index(str_value):
    index_h = str_value.find('h')
    if index_h > 1:
        return str_value[index_h:]
    else:
        return str_value

df['education_substring'] = df['parental level of education'].apply(lambda x: find_substring_if_h_index(str(x)))

print(df[['parental level of education', 'education_substring']])