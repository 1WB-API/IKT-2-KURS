print('ПРАКТИЧЕСКАЯ №(1)')
print('А)')
x=1
y=2
t=2
c = (x+3*y*t-4)/(0.3*x*y*t)
print(c)

print('')

print('Б)')
h = int(input('Введите часы: '))
m = int(input('Введите минуты: '))
if (h == 10 and m >= 10) or (h == 11 and m < 50):
    print('Преподаватель занят.')
    
elif (h == 13 and m >= 30) or (h == 14) or (h == 15 and m < 0):
    print('Преподаватель занят.')
    
elif (h == 16 and m >= 50) or (h == 17) or (h == 18 and m < 20):
    print('Преподаватель занят.')
    
else:
    print('Преподаватель свободен.')