lst = []
print(lst, type(lst))
lst = list('Hello World!')
print(lst)

lst = [1, 2, 3, 4, 5, 6]

lst = [1, 4.5, 'test', True, [4, 6, 'g']]
print(lst)

print(lst[2])
lst[2] = 4444
print(lst)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = lst1 + lst2
print(lst3)

lst3 = lst1 * 3
print(lst3)

for element in lst3:
    print(element, end=' ')
print()

for i in range(len(lst3)):
    print(lst3[i], end=' ')
print()


# len(list) = передаем на вход список получаем количество результатов в этом списке

print(len(lst3))

# A in list - присутвует ли в нашем списке лист переменная A
# A not in list
print(3 in lst3)
print(4 in lst3)
print(3 not in lst3)
print(4 not in lst3)

# min, max, sum = позволяет определить максимальное, минимальное и сумму

print(min(lst3))
print(max(lst3))
print(sum(lst3))

# если нужно получить индекс значения в списке list.index(A)
# в качестве параметра принмает значения которое нужно определить

print(lst3.index(3, 6))

# list.count(value) позволяет получить количество значений в список
print(lst3.count(3))

# list.pop() вернет значение последнего
# list.pop(index) вернет значение элемента по указоному индексу ( удаляет)
print(lst3)
print(lst3.pop(4))
print(lst3)

# list.append(value)
lst3.append(555)
print(lst3)

# # list.insert(index, value) принимает два параметра первый указывает позицию
# # второй хранит то значение которое мы хотим добавить в список
# lst3.insert(4, 777)
# print(lst3)
#
# # list.clear() позволяет очистить список от элементов
# lst3.clear()
# print(lst3)


# list.copy()
print(id(lst3), lst3)
lst4 = lst3
print(id(lst4), lst4)

lst3[5] = 888
print(lst4)

lst4 = lst3.copy()
print(id(lst3), lst3)
print(id(lst4), lst4)
lst3[5] = 0
print(lst4)
# lst4 = lst3[:]

# list1.extend(list2) позволяет расширить текущий список как операция сложения
# list1 + list2

print(lst1, lst2)
lst1.extend(lst2)
print(lst1, lst2)


# list.remove(value) принмает в качестве параметра значение которое нужно удалить
# del element
print(lst3)
lst3.remove(555)
print(lst3)
del lst3[2]
print(lst3)
# del lst3
# print(lst3)

# list.revers() позволяет первернуть список
# как с использовением срезов
# list[:: -1]
print(id(lst3), lst3)
lst3.reverse()
print(id(lst3), lst3)
lst4 = lst3[:: -1]
print(id(lst4), lst4)

# list.sort() упорядочивание элементов списка
# для того чтобы упорядочить по убыванию
# lst3.sort(reverse=True)
lst3.sort(reverse=True)
print(lst3)
lst3.sort()
print(lst3)

