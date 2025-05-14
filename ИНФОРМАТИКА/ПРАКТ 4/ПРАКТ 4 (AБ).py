# Практическая работа № 4
# Основы работы с Python. Словари и анализ данных из файла

# =========================
# Задание 4.1. Работа со словарями
# =========================

# 1. Создание словаря
# Словарь — это изменяемая структура данных, которая хранит пары ключ-значение.
# Каждый ключ в словаре уникален и связан с определённым значением.
book_info = {
    'title': 'Война и мир',
    'author': 'Лев Толстой',
    'year': 1869,
    'genres': ['роман', 'исторический']
}
# В данном случае, словарь содержит информацию о книге с ключами: 'title', 'author', 'year', 'genres'.

# 2. Обращение к ключам словаря
# Чтобы получить значение по ключу, используем синтаксис dict[key]
print("Название книги:", book_info['title'])
# Вывод: Название книги: Война и мир

# Если обратиться к несуществующему ключу, произойдет ошибка KeyError.
# Например:
# print(book_info['publisher'])  # Это вызовет ошибку, так как ключ 'publisher' ещё не добавлен.

# 3. Метод setdefault()
# Метод setdefault(key, default) возвращает значение по ключу, если он есть,
# или добавляет в словарь ключ с указанным значением, если ключ отсутствует.
# Это удобно для инициализации новых ключей без риска перезаписать существующие.
# Используем его для добавления информации о издателе.
publisher = book_info.setdefault('publisher', 'Издательство АСТ')
print("Издательство:", publisher)
# Вывод: Издательство: Издательство АСТ

# Теперь в словаре есть новый ключ 'publisher'.
print("Обновленный словарь book_info:", book_info)

# 4. Перебор элементов словаря
# Можно проходить по ключам, по значениям или по парам ключ-значение.
print("\nПеребор по ключам:")
for key in book_info:
    print(f'Ключ: {key} -> Значение: {book_info[key]}')
# Перебор по ключам и вывод значений

print("\nПеребор по значениям:")
for value in book_info.values():
    print(f'Значение: {value}')

print("\nПеребор по ключам и значениям одновременно:")
for key, value in book_info.items():
    print(f'{key}: {value}')

# =========================
# Задание 4.2. Вложенные структуры
# =========================

# 1. Вложенные списки
# Список — это упорядоченная изменяемая коллекция элементов.
# Вложенные списки — это списки внутри других списков.
grades = [
    ['Иван', 85, 90],
    ['Мария', 92, 88],
    ['Петр', 78, 83]
]
# grades — список списков, где каждый внутренний список содержит имя и оценки.

# 2. Проход по вложенному списку. Фильтрация
# Получим список студентов, у которых первая оценка больше 85.
high_scorers = [student for student in grades if student[1] > 85]
print("\nСтуденты с оценкой выше 85 по первому предмету:", high_scorers)

# 3. Вложенные словари
# Словарь — это структура данных, хранящая пары ключ-значение.
# Вложенные словари — это словари внутри других словарей.
employees = {
    'emp1': {'name': 'Алексей', 'department': 'IT', 'salary': 60000},
    'emp2': {'name': 'Ольга', 'department': 'HR', 'salary': 55000},
    'emp3': {'name': 'Борис', 'department': 'IT', 'salary': 65000}
}
# Здесь каждый сотрудник представлен словарём с данными.

# 4. Фильтрация вложенных словарей
# Например, найти всех сотрудников из отдела 'IT'.
it_employees = {k: v for k, v in employees.items() if v['department'] == 'IT'}
print("\nСотрудники из отдела IT:", it_employees)

# =========================
# Задание 4.3. Структуры для хранения данных в файлах
# =========================

import json
from collections import Counter

# 1. JSON-файл — это текстовый файл, содержащий структурированные данные в формате JSON.
# Предполагается, что файл data.json уже скачан и находится в текущей директории.

# 2. Открытие JSON-файла в Python
# Для этого используется встроенная библиотека json.
try:
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    print("\nФайл data.json успешно открыт и загружен.")
except FileNotFoundError:
    print("\nФайл data.json не найден. Пожалуйста, убедитесь, что файл находится в той же директории.")
    data = {}

# 3. Работа с данными
if data and isinstance(data, dict) and 'events_data' in data:
    events = data['events_data']
    # Предположим, что events — список словарей с ключами: id, client_id, user_id, category, action, options.

    # Используем Counter для подсчёта частоты различных action
    actions = [event['action'] for event in events]
    action_counts = Counter(actions)
    print("\nРаспределение действий (top 5):")
    for action, count in action_counts.most_common(5):
        print(f'{action}: {count}')

    # Анализ данных: подсчёт уникальных клиентов
    client_ids = [event['client_id'] for event in events]
    print(f"\nОбщее количество событий: {len(events)}")
    print(f"Количество уникальных клиентов: {len(set(client_ids))}")
else:
    print("\nДанные из файла недоступны или структура неправильная.")




#===========================================================================================
#===========================================================================================
#===========================================================================================

print("ПРАКТИЧЕСКАЯ №4(A)")

countries = ['Россия', 'Германия', 'Франция', 'Италия', 'Испания', 'Великобритания']
cities = ['Москва', 'Берлин', 'Париж', 'Рим', 'Мадрид', 'Лондон', 'Киев']

text = """
Я путешествовал по Москве и Парижу. В Германии я был в Берлине, а в Италии — в Риме.
Также я посетил Мадрид и Киев. В Лондоне мне очень понравилось.
"""
found_countries = []
found_cities = []

for country in countries:
    if country[:-1] in text:
        found_countries.append(country)

for city in cities:
    if city[:-1] in text:
        found_cities.append(city)

print("Найдены страны:", found_countries)
print("Найдены города:", found_cities)



print("")
print("ПРАКТИЧЕСКАЯ №4(Б)")

import json

with open("data.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

events = data.get('events_data', [])

all_clients = set()
with_actions = set()

for event in events:
    client_id = event.get('client_id')
    category = event.get('category')
    all_clients.add(client_id)
    if category in ['datepicker', 'table']:
        with_actions.add(client_id)

without_actions = all_clients - with_actions

count_cwa = len(without_actions)

print("Количество клиентов, не совершавших действий с категориями 'datepicker' и 'table':", count_cwa)