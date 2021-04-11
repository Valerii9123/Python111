import random

"""


                1      /        2
new_list = [ expression for item in list ]
1  колистве этераций( действий) 
2  
 or 
 
 new_list = [ expression for item in list if conditional ] 
"""


lst0 = []
for _ in range(15):
    lst0.append(round(random.uniform(1, 100), 2))


lst1 = [round(random.uniform(1, 100), 2) for _ in range(15)]
print(lst1)

lst2 = [element for element in lst1 if element > 20]
print(lst2)

