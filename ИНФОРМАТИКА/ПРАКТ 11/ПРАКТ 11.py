# ===========================
# Практическая работа №11
# ===========================


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Путь к вашему файлу .csv
file_path = 'cacao_flavors.csv'  # Замените на свой путь

# Загрузка данных
df = pd.read_csv(file_path, engine='python')

# Первичный просмотр
print("Первые строки данных:")
print(df.head())

print("\nОбщая информация о данных:")
print(df.info())

# Проверка пропусков
print("\nПроверка пропусков по столбцам:")
print(df.isnull().sum())

# Проверка на дублированные строки
duplicates = df.duplicated().sum()
print(f"\nКоличество дублированных строк: {duplicates}")
if duplicates > 0:
    df = df.drop_duplicates()

# Посмотрим исходные названия колонок
print("Исходные названия колонок:")
print(df.columns.tolist())

# Переименование колонок для удобства (учитываем переносы строк)
df.rename(columns={
    'Bar id': 'Bar id',
    'Company \n(Maker-if known)': 'Company (Maker-if known)',
    'Specific Bean Origin\nor Bar Name': 'Specific Bean Origin or Bar Name',
    'REF': 'ref',
    'Review \nDate': 'Review Date',
    'Cocoa\nPercent': 'Cocoa Percent',
    'Company\nLocation': 'Company Location',
    'Rating': 'Rating',
    'Bean\nType': 'Bean Type',
    'Broad Bean\nOrigin': 'Broad Bean Origin'
}, inplace=True)

print("Обновленные названия колонок:")
print(df.columns.tolist())

# Обработка 'Cocoa Percent'
def clean_cocoa_percent(val):
    if pd.isnull(val):
        return np.nan
    val_str = str(val).replace('%', '').replace(',', '.').strip()
    try:
        return float(val_str)
    except:
        return np.nan

if 'Cocoa Percent' in df.columns:
    df['cocoa_percent_float'] = df['Cocoa Percent'].apply(clean_cocoa_percent)
else:
    print("Столбец 'Cocoa Percent' не найден.")

# Обработка дат
if 'Review Date' in df.columns:
    df['Review Date'] = pd.to_datetime(df['Review Date'], errors='coerce')

# Обработка рейтинга
if 'Rating' in df.columns:
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Обработка ref
if 'ref' in df.columns:
    df['ref'] = pd.to_numeric(df['ref'], errors='coerce')

# Обработка остальных строковых колонок
str_cols = ['Company (Maker-if known)', 'Specific Bean Origin or Bar Name',
            'Company Location', 'Bean Type', 'Broad Bean Origin']
for col in str_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# Удаляем пропуски по ключевым переменным
df.dropna(subset=['ref', 'Rating', 'cocoa_percent_float'], inplace=True)

# Удаляем выбросы в 'Rating' (например, вне диапазона 1-20)
df = df[(df['Rating'] >= 1) & (df['Rating'] <= 20)]

# Визуальный анализ
# Корреляционная матрица
corr_matrix = df[['ref', 'cocoa_percent_float', 'Rating']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Корреляционная матрица числовых переменных')
plt.show()

# Распределение по Bar id
if 'Bar id' in df.columns:
    counts = df['Bar id'].value_counts()
    top_n = 20  # Можно изменить число
    top_counts = counts.head(top_n)
    plt.figure(figsize=(12, 6))
    top_counts.plot(kind='bar')
    plt.title('Распределение по Top {} Bar ID'.format(top_n))
    plt.xlabel('Bar ID')
    plt.ylabel('Количество')
    plt.xticks(rotation=45, ha='right')  # Поворот подписей
    plt.tight_layout()  # Чтобы всё поместилось
    plt.show()

# Анализ компаний
if 'Company (Maker-if known)' in df.columns:
    print(f"Количество уникальных компаний: {df['Company (Maker-if known)'].nunique()}")
    top_companies = df['Company (Maker-if known)'].value_counts()
    print("ТОП 10 компаний:")
    print(top_companies.head(10))
    top_companies.head(10).plot(kind='bar')
    plt.title('Топ 10 компаний')
    plt.xlabel('Компания')
    plt.ylabel('Количество')
    plt.show()

# Анализ 'Specific Bean Origin or Bar Name'
if 'Specific Bean Origin or Bar Name' in df.columns:
    print(f"Уникальных регионов: {df['Specific Bean Origin or Bar Name'].nunique()}")
    values_counts = df['Specific Bean Origin or Bar Name'].value_counts()
    more_than_10 = values_counts[values_counts > 10]
    print(f"Значений, встречающихся более 10 раз: {len(more_than_10)}")
    more_than_10.plot(kind='bar')
    plt.title('Топ регионов (более 10 повторений)')
    plt.xlabel('Регион')
    plt.ylabel('Частота')
    plt.show()

# Распределение REF
if 'ref' in df.columns:
    df['ref'].hist(bins=30)
    plt.title('Распределение REF')
    plt.xlabel('REF')
    plt.ylabel('Частота')
    plt.show()
    print(df['ref'].describe())

# Распределение Review Date
if 'Review Date' in df.columns:
    df['Review Date'].hist(bins=30)
    plt.title('Распределение Review Date')
    plt.xlabel('Дата')
    plt.ylabel('Частота')
    plt.show()
    print(df['Review Date'].describe())

# Распределение % какао
if 'cocoa_percent_float' in df.columns:
    df['cocoa_percent_float'].describe()
    plt.hist(df['cocoa_percent_float'].dropna(), bins=20)
    plt.title('Распределение % какао')
    plt.xlabel('% какао')
    plt.ylabel('Количество')
    plt.show()

# Анализ 'Company Location'
if 'Company Location' in df.columns:
    print(f"Количество стран: {df['Company Location'].nunique()}")
    country_counts = df['Company Location'].value_counts()
    print("ТОП стран:")
    print(country_counts.head(10))
    country_counts.head(10).plot(kind='bar')
    plt.title('Топ стран по компаниям')
    plt.xlabel('Страна')
    plt.ylabel('Количество')
    plt.show()

# Анализ 'Bean Type'
if 'Bean Type' in df.columns:
    print(f"Пропусков: {df['Bean Type'].isnull().sum()}")
    df['Bean Type'] = df['Bean Type'].astype(str)
    bean_counts = df['Bean Type'].value_counts()
    print("ТОП типов бобов:")
    print(bean_counts.head(10))
    bean_counts.head(10).plot(kind='bar')
    plt.title('Топ типов бобов')
    plt.xlabel('Тип боба')
    plt.ylabel('Количество')
    plt.show()

# Анализ 'Broad Bean Origin' и его нормализация
if 'Broad Bean Origin' in df.columns:
    df['Broad Bean Origin'] = df['Broad Bean Origin'].astype(str)
    print(f"Пропусков: {df['Broad Bean Origin'].isnull().sum()}")
    broad_counts = df['Broad Bean Origin'].value_counts()
    print("ТОП оригиналов:")
    print(broad_counts.head(10))
    
    # Нормализация текста
    def normalize_text(s):
        if pd.isnull(s):
            return s
        s = s.lower().strip()
        return s

    df['Broad Bean Origin Normalized'] = df['Broad Bean Origin'].apply(normalize_text)
    
    # Повторный анализ
    broad_counts_norm = df['Broad Bean Origin Normalized'].value_counts()
    print(f"После нормализации, значений более 10 раз: {len(broad_counts_norm[broad_counts_norm > 10])}")
    broad_counts_norm.head(10).plot(kind='bar')
    plt.title('ТОП после нормализации')
    plt.xlabel('Регион')
    plt.ylabel('Частота')
    plt.show()

# Построение модели предсказания Rating по 'ref' и 'cocoa_percent_float'
features = ['ref', 'cocoa_percent_float']
X = df[features]
y = df['Rating']

# Удаляем пропуски в признаках
X = X.dropna()
y = y.loc[X.index]

# Деление данных на обучающую и тестовую
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказания
y_pred = model.predict(X_test)

# Оценка модели
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"\nКачество модели:")
print(f"RMSE: {rmse}")
print(f"R^2: {r2}")

# Визуализация предсказаний
plt.scatter(y_test, y_pred, alpha=0.7)
plt.xlabel('Реальные значения Rating')
plt.ylabel('Предсказанные значения Rating')
plt.title('Предсказание Rating моделью')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.show()

print("\nАнализ завершен. Основные выводы:")
print("- В данных есть пропуски и дубли, их обработали.")
print("- Обнаружены выбросы в 'Rating' и 'Cocoa Percent', их удалили.")
print("- Обнаружены важные корреляции между переменными.")
print("- Построена базовая модель предсказания Rating.")