"""
while <condition>:
    operator 1
    operator 2
    operator 3

operator 4
Один круг выполнения цикла называется интерация
Если цикл не правда он прекращаеться либо пропускается
Пока условия истина мы крутимся в цикле


"""
a = 1
while a <= 10:
    print(a, end=' ')
    a += 1

print()

"""
    for variable in < iterable_object>: 
    operator 1
    operator 2 
    operator 3
    variable - название цикла for. Может быть любым
    
for _ in <iterable_object>:
    operator 1
    operator 2
    operator 3
    
"""

for s in '1 2 3 4 5 6 7 8 9 10':
    print(s, end=' ')
print()


# range ( позволяет получить числа в определенном диапазоне )
# range(star, stop, step)
# range(start, step)
# range(stop)
# range(1, 10)

for var in range(2, 11, 2):
    print(var, end=' ')
print()

s = 'Process finished with exit code 0'
for v in range(33):
    print(s[v], end=' ')
print()

# break - прерывает работу цикла

for v in s:
    if v != ' ':
        print(v, end='')
    else:
        break
print()

# continue - позволяет прервать текущую этерацию и вернуться в начало
# else
s = 'Process-finished-with-exit-code-0'
for v in s:
    if v != ' ':
        print(v, end='')
    else:
        break
else:
    print('end')

print()


# пример ДЗ
"""
50     5 32       2 ** = 32
вывести степень двойки и возводение двойки в эту степень и результат должен быть меньше чем значение использовать цикл while
и оператор if 

чтобы организовать бесконечный цикл требуется 
while True:

чтобы завершить нужен оператор if
"""
num = 0
while True:

    if num == 0:
        break
