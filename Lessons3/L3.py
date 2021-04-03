"""
if <condition>:
    operator1
    operator2

if < <condition 1>:

elif <condition 2>:


else:


"""
# a = int(input('Введите число: '))
# if a >= 10 and a <= 20:
#     print('Our number is negative')
# else:
#     print('Number is incorrect')
# print('end')
#
# a = int(input('Введите число: '))
# if a > 0:
#     print("Positive")
# elif a < 0:
#     print('Negative')
# else:
#     print('Zero')
#
# print('End')

# result = a ? b : c ( скоращенная структура if else )
a = int(input('Введите число: '))
res = 'Our number in range from 10 to 20' if 10 <= a <= 20 else 'Number is incorrect'
print(res)

