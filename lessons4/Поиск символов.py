

st1 = input('Введите строку: ')
s1 =st1[st1.find('h')+1:st1.rfind('h')]
s2 = s1.replace('h', 'H')
st2 = st1[:st1.find('h')+1]+s2+st1[st1.rfind('h')]
print(st2)






