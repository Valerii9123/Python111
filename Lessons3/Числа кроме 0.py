a = 0
b = 0  # количество введеных чисел
c = 0  # сумма ведденых чисел
d = 0  # среднее значение
positive = 0  # количесвто четных чисел
negative = 0  # количество нечетных чисел
x = 0  # наибольшее значение
y = 0  # наименьшее значение


while True:
    num = int(input('Enter Number: '))
    if num == 0:
        break
    else:
        b += 1
        c += num
        d = c // b
        positive += num % 2 == 0
        negative += num % 2 != 0
        if num > x == 0:
            x = num
        if num < y == 0:
            y = num

print('Количество чисел: ', b)
print('Сумма Чисел: ', c)
print('Среднее арифметическое: ', d)
print('Четных чисел: ', positive)
print('Количество не четных: ', negative)
print('Максимальное значение: ', x)
print('Минимальное значение: ', y)
print()
