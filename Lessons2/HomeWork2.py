# Сколько парт нужно закупить, если за партой может сидеть только 2 ученика/


a = int(input ("Количество учеников в первом классе"))
b = int(input ("Количество учеников во втором классе"))
c = int(input ("Количество учеников в третьем классе"))
d = (a//2 + b//2 + c//2 + a%2 + b%2 + c%2)




print("Требуемое количество парт " + str(d))


