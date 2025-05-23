# ===========================
# Цикл с параметром (for)
# ===========================

print("=== Цикл for с range() ===")
# Пример 1: вывод чисел от 0 до 4
for i in range(5):
    print(i, end=' ')  # 0 1 2 3 4
print("\n")

# Пример 2: числа от 1 до 9 с шагом 2
for i in range(1, 10, 2):
    print(i, end=' ')  # 1 3 5 7 9
print("\n")

# ===========================
# Использование enumerate()
# ===========================

fruits = ['яблоко', 'банан', 'апельсин']
print("=== Перебор списка с enumerate() ===")
for index, fruit in enumerate(fruits):
    print(f"Индекс: {index}, Фрукт: {fruit}")
print()

# ===========================
# Управление выполнением цикла
# ===========================

print("=== break и continue ===")
# break: прерывает цикл
print("Пример break:")
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
print("\n")

# continue: пропускает текущую итерацию
print("Пример continue:")
for i in range(5):
    if i == 2:
        continue
    print(i, end=' ')
print("\n")

# ===========================
# Практический пример (задание А)
# Вывод чисел от 1 до 10, пропуская 5
print("=== Вывод чисел от 1 до 10, пропуская 5 ===")
for num in range(1, 11):
    if num == 5:
        continue
    print(num, end=' ')
print("\n")

# ===========================
# Цикл с условием (while)
# ===========================

print("=== Цикл while для суммы чисел до 0 ===")
total = 0
while True:
    num = int(input("Введите число (0 для выхода): "))
    if num == 0:
        break
    total += num
print("Сумма введенных чисел:", total)


#===========================================================================================
#===========================================================================================
#===========================================================================================


print('ПРАКТИЧЕСКАЯ №(2)')
print('A)')

a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
sumsq = 0
sumcub = 0
for n in range(a, b + 1):
    if n % 2 == 0:
        sumsq += n ** 2
    if n % 3 == 0:
        sumcub += n ** 3
print('Сумма квадратов чисел, делящихся на 2: ', sumsq)
print('Сумма кубов чисел, делящихся на 3: ', sumcub)

print('')

print('Б)')

lim= 400
total = 0

while True:
    weight = int(input('Введите вес человека (или 0 для выхода): '))
    
    if weight == 0:
        break
    total += weight

    if total > lim:
        final = total - lim
        print(f'Перевес {final} кг')
    else:
        print('Вес в пределах нормы')