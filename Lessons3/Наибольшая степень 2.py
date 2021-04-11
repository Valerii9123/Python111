a = 1
b = 0
num = int(input('Enter number: '))
while a <= num:
    a *= 2
    b += 1
    if a <= num:
        print(b, a, end='    ')
    else:
        continue
print(b, a)





