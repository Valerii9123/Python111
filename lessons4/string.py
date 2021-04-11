# a = 123456789123456789 #- десятичное число
# print(a)
# print(bin(a))  # - перевод в двоичную
# print(oct(a))  #  - перевод в 8 битную систему
# print(hex(a))  # перевод в 16ти ричную

print(chr(0x26bd))  #  0x - говорит о том что дальше идет 16тиричный код
print('\u26bd')   # \u для обозначения в строке юникод символа # \U разница между большим и маленьким размер байтов в символе
# # \u - 2 bites   \U - 4 bites:  каждая пара цифр описывает 1 байт
# print(chr(9917))
#
# print(ord('⚽')) # функция переводит символ в десятиричный код чтобы перевести в другую нужно перед орд выставить значения
#
#
# #   -5 -4  -3  -2  -1
# #    H  E   L   L   O
# #    0  1   2   3   4
# print(string[0])
# print(string[len(string)-1])
# print(string[-1])
# print(string[34])
# print(string[-35])
# string[3] = 'A' - так нельзя менять строку
# print(string)

# str[start: stop: step] (стоп -1( не входит в вывод среза)
# str[:] - обозначаем всю строку

string = 'Process finished with exit code 0'
print(string[0])
print(string[0:7])
print(string[8: -1])
print(string[8: 16: 2]) # 2-шаг + 2 к началу 8
print(string[:: -1]) #  строка наооборот
print(string[:: -2]) #  напишет с обратной стороны через 1 символ
print(string[:: 2]) # выбираем только с четным индексом
print(string[1:: 2]) # выводим с нечетными индексами

s = 'Process finished with exit code 0'
# len(str) позволяет получить длину строки
print(len(s))

# find - позволяет выполнить поиск под строки в строке вхождение с начала строки
# find(sub, star, end) первы параметр обязателен  второй и третий не обязательны
print(s.find('it', 19)) # -1 ничего не нашли
# rfind - ищет с конца вхождение с конца

# replace(old, new, count) old - что ищем new  - что меняем count - количество действий

s2 = s.replace('e', 'E')
print(s2)

# count(sub, start, end) sub - что мы считаем star, end - откуда до куда

print(s.count('e', 0, 8))

# capitalize() выолняет перевод всех символов строки на нижний регистр но первую букву переводит в верхний

s = 'finished with exit code'
print(s.capitalize())

# upper() - переводи все символы строки на верхний регистр

# lower() - переводит все символы в нижний регистр

s3 = s.upper()
print(s3)
print(s3.lower())
# strip(sub) может принмать параметр подстроку
# удаляет и слева и справа ненужные символы


s = '    finished with exit code        '
print('('+ s+ ')')
print('(' + s.strip() + ')')
s2 = 'aaaaaaaaaafinished with exit codebbbbbbbb'
print(s2)

s4 = s2.strip()
s5 = s4.strip('a')



# title переводит все символы в нижний регистр кроме  первых символов каждого слова
print(s2.title())

