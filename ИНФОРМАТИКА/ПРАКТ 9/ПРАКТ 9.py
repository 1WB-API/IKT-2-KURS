# ===========================
# Практическая работа №9
# ===========================


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
tips = pd.read_csv('tips.csv')

# 1. Основные понятия
# - Случайная величина: например, 'total_bill' — сумма заказа
# - Наблюдение: конкретное значение 'total_bill' в одной строке
# - Генеральная совокупность: все заказы в файле
# - Выборка: случайно выбранные заказы (например, все строки)

# 2. Выборочное среднее и истинное среднее
# Среднее — сумма всех значений делённая на их число
sample_mean_total_bill = tips['total_bill'].mean()
# Математическое ожидание (истинное среднее) неизвестно, используем выборочное
print(f"Выборочное среднее total_bill: {sample_mean_total_bill:.2f}")

# Как среднее реагирует на выбросы?
# Добавим выброс
tips_with_outlier = tips.copy()
tips_with_outlier.loc[0, 'total_bill'] = tips['total_bill'].max() * 10
mean_with_outlier = tips_with_outlier['total_bill'].mean()
print(f"Среднее с выбросом: {mean_with_outlier:.2f}")
# Среднее очень чувствительно к выбросам

# 3. Медиана
median_total_bill = tips['total_bill'].median()
print(f"Медиана total_bill: {median_total_bill:.2f}")

# Как медиана реагирует на выбросы?
# Добавим выброс
tips_with_outlier.loc[0, 'total_bill'] = tips['total_bill'].max() * 10
median_with_outlier = tips_with_outlier['total_bill'].median()
print(f"Медиана с выбросом: {median_with_outlier:.2f}")
# Медиана менее чувствительна к выбросам

# 4. Мода
mode_time = tips['time'].mode()[0]
print(f"Мода по 'time': {mode_time}")
# Например, самый популярный день
mode_day = tips['day'].mode()[0]
print(f"Мода по 'day': {mode_day}")

# 5. Квартили (эксклюзивный метод)
# Эксклюзивный метод — у numpy (method='exclusive')
q1_excl = np.percentile(tips['total_bill'], 25, method='linear')
q2_excl = np.percentile(tips['total_bill'], 50, method='linear')
q3_excl = np.percentile(tips['total_bill'], 75, method='linear')
print("Квартили (эксклюзив):")
print(f"Q1: {q1_excl:.2f}")
print(f"Q2 (медиана): {q2_excl:.2f}")
print(f"Q3: {q3_excl:.2f}")

# 6. Меры разброса
iqr = q3_excl - q1_excl
std_dev = tips['total_bill'].std()
print(f"Межквартильный размах (IQR): {iqr:.2f}")
print(f"Стандартное отклонение: {std_dev:.2f}")

# 7. График - гистограмма распределения 'total_bill'
plt.figure(figsize=(8,5))
tips['total_bill'].plot(kind='hist', bins=20, alpha=0.7, color='skyblue')
plt.title('Распределение total_bill')
plt.xlabel('Total Bill')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

# 8. График с категориальными переменными: bar-график для 'sex'
plt.figure(figsize=(6,4))
tips['sex'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Распределение по полу')
plt.xlabel('Пол')
plt.ylabel('Количество')
plt.grid(axis='y')
plt.show()

# 9. Распределение 'total_bill' по полу (две переменные)
plt.figure(figsize=(8,6))
sns.boxplot(x='sex', y='total_bill', data=tips)
plt.title('Распределение total_bill по полу')
plt.xlabel('Пол')
plt.ylabel('Total Bill')
plt.show()

# 10. Распределение по времени суток (обед/ужин)
plt.figure(figsize=(8,6))
sns.boxplot(x='time', y='total_bill', data=tips)
plt.title('Распределение total_bill по времени')
plt.xlabel('Время')
plt.ylabel('Total Bill')
plt.show()

# 11. Распределение заказов по дням недели
plt.figure(figsize=(8,6))
sns.countplot(x='day', data=tips, palette='Set2')
plt.title('Количество заказов по дням недели')
plt.xlabel('День недели')
plt.ylabel('Количество')
plt.grid(axis='y')
plt.show()

# 12. Корреляционная матрица и heatmap
# Получение только числовых столбцов
numeric_cols = tips.select_dtypes(include=[np.number])

# Вычисление корреляционной матрицы только для числовых данных
corr_matrix = numeric_cols.corr()

# Построение тепловой карты
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Тепловая карта корреляций')
plt.show()

# 13. Метод distplot() (устаревший), используем seaborn.histplot()
plt.figure(figsize=(8,5))
sns.histplot(tips['total_bill'], kde=True)
plt.title('Распределение total_bill с KDE')
plt.xlabel('Total Bill')
plt.ylabel('Плотность')
plt.show()

# 14. Метод countplot() для категориальной переменной 'smoker'
plt.figure(figsize=(6,4))
sns.countplot(x='smoker', data=tips, palette='pastel')
plt.title('Количество курящих и некурящих')
plt.xlabel('Курит')
plt.ylabel('Количество')
plt.grid(axis='y')
plt.show()

# 15. Метод boxplot() для 'size' — число посетителей
plt.figure(figsize=(8,6))
sns.boxplot(x='size', y='total_bill', data=tips)
plt.title('Распределение total_bill по размеру группы')
plt.xlabel('Количество посетителей')
plt.ylabel('Total Bill')
plt.show()

# 16. Использование axes() и hist() из matplotlib
fig, ax = plt.subplots()
ax.hist(tips['total_bill'], bins=20, color='purple', alpha=0.7, label='total_bill')
ax.set_title('Гистограмма total_bill')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Частота')
ax.legend()
plt.show()

# 17. Обзор: краткое описание
print("Общее описание данных:\n", tips.describe())



#===========================================================================================
#===========================================================================================
#===========================================================================================

print("")
print("ПРАКТИЧЕСКАЯ №(9)")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')

grouped = df.groupby(['day', 'smoker'])['tip'].mean().reset_index()

days_order = ['Sun', 'Sat', 'Thur', 'Fri']
grouped['day'] = pd.Categorical(grouped['day'], categories=days_order, ordered=True)
grouped = grouped.sort_values('day')

pivot_table = grouped.pivot(index='day', columns='smoker', values='tip')

plt.figure(figsize=(8, 6))
sns.lineplot(data=pivot_table, marker='o')

plt.title('Средний размер чаевых по дням недели\nдля курящих и некурящих')
plt.xlabel('День недели')
plt.ylabel('Средние чаевые')
plt.legend(title='Курение', labels=['Нет', 'Да'])
plt.grid(True)
plt.show()