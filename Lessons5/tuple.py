#   признаком кортежа является " , "
#  кортедж это встроенная последовательность или колекция

tup = ()
print(tup, type(tup))
tup = tuple('Hello World!')
print(tup, type(tup))
tup = (1, 2, 3, 4, 5, 6, 'test, False')
print(tup, type(tup))

t1 = (1, 2, 3)
t2 = (4, 5,6)
t3 = t1 + t2
print(t3)
t4 = t3 * 4
print(t4)

t5 = (50, 67, 78) # запаковка кортеджа

a, b, c = t5 # распаковка кортеджа
print(a, b, c)

a = t5[0]
b = t5[1]
c = t5[2]
