# ===========================
# Практическая работа №10
# ===========================


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Загрузка данных
data = pd.read_csv('mycar_lin.csv')

# Предварительный анализ
print("Исходные данные:")
print(data.describe())

# Функция для удаления выбросов по межквартильному диапазону (IQR)
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Удаляем выбросы из исходных данных
data_no_outliers = remove_outliers_iqr(data, 'Stopping_dist')
data_no_outliers = remove_outliers_iqr(data_no_outliers, 'Speed')

# Визуализация исходных данных до группировки
plt.figure(figsize=(8, 6))
plt.plot(data['Speed'], data['Stopping_dist'], 'o', linestyle='None', color='blue')
plt.xlabel('Speed (км/ч)')
plt.ylabel('Тормозной путь (м)')
plt.title('Исходные данные: тормозной путь от скорости')
plt.show()

# Визуализация без выбросов
plt.figure(figsize=(8, 6))
plt.plot(data_no_outliers['Speed'], data_no_outliers['Stopping_dist'], 'o', linestyle='None', color='green')
plt.xlabel('Speed (км/ч)')
plt.ylabel('Тормозной путь (м)')
plt.title('Данные без выбросов')
plt.show()

# Группировка по скорости и усреднение тормозного пути
data_grouped = data_no_outliers.groupby('Speed', as_index=False)['Stopping_dist'].mean()

# Визуализация сгруппированных данных
plt.figure(figsize=(8, 6))
plt.plot(data_grouped['Speed'], data_grouped['Stopping_dist'], 'o-', color='orange')
plt.xlabel('Speed (км/ч)')
plt.ylabel('Средний тормозной путь (м)')
plt.title('Средние значения тормозного пути по скорости')
plt.show()

# Построение boxplot для проверки распределений
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(x=data_no_outliers['Stopping_dist'])
plt.title('Распределение тормозного пути после очистки')
plt.subplot(1, 2, 2)
sns.boxplot(x=data_no_outliers['Speed'])
plt.title('Распределение скорости после очистки')
plt.show()

# Обучение модели на сгруппированных данных
X = data_grouped[['Speed']]
y = data_grouped['Stopping_dist']

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказания на тестовой выборке
y_pred = model.predict(X_test)

# Вывод метрик
print(f'Метрики модели:')
print(f'MAE: {mean_absolute_error(y_test, y_pred):.2f}')
print(f'RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}')
print(f'R²: {r2_score(y_test, y_pred):.2f}')
print(f'Коэффициент наклона (угол): {model.coef_[0]:.2f}')
print(f'Свободный член: {model.intercept_:.2f}')

# Визуализация линий и точек
# Сортируем сгруппированные точки для правильного отображения
data_sorted = data_grouped.sort_values(by='Speed')

plt.figure(figsize=(10, 6))
# Построение линий между усреднёнными точками
plt.plot(data_sorted['Speed'], data_sorted['Stopping_dist'], 'o-', color='orange', label='Средние значения')

# Построение линии регрессии по этим точкам
X_plot = data_sorted['Speed'].values.reshape(-1, 1)
y_plot = model.predict(X_plot)
plt.plot(data_sorted['Speed'], y_plot, color='red', linewidth=2, label='Линия регрессии')

# Также показать все исходные реальные точки
plt.scatter(data['Speed'], data['Stopping_dist'], s=10, alpha=0.3, label='Все исходные точки', color='blue')

plt.xlabel('Speed (км/ч)')
plt.ylabel('Тормозной путь (м)')
plt.title('Регрессия тормозного пути по скорости')
plt.legend()
plt.show()

# Теперь добавляем линии, соединяющие все реальные точки сгруппированы по скорости
plt.figure(figsize=(10, 6))
# Все реальные точки (по исходным данным)
plt.scatter(data['Speed'], data['Stopping_dist'], s=10, alpha=0.3, label='Все исходные точки', color='lightblue')

# Все сгруппированные средние точки
plt.plot(data_sorted['Speed'], data_sorted['Stopping_dist'], 'o-', color='orange', label='Средние значения')

# Линии, соединяющие средние точки
plt.plot(data_sorted['Speed'], data_sorted['Stopping_dist'], linestyle='-', color='orange')

# Линия регрессии
plt.plot(data_sorted['Speed'], y_plot, color='red', linewidth=2, label='Линия регрессии')

plt.xlabel('Speed (км/ч)')
plt.ylabel('Тормозной путь (м)')
plt.title('Все точки и линия регрессии с соединением группированных средних')
plt.legend()
plt.show()

# Итог
print("Анализ завершён.")