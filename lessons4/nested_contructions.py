rows = 11
cols = 11

for i in range(rows):
    # print(i, end='\t')
    for j in range(cols):
        if i == 0 or j == 0 or i == rows-1 or j == cols-1:
            print('* ', end='')
        else:
            print('  ', end='')

    print()

print()

for i in range(rows):
    # print(i, end='\t')
    for j in range(cols):
        if (i == 0 or j == 0 or i == rows-1 or j == cols-1
        or i == j or i == cols - j -1):
            print('* ', end='')
        else:
            print('  ', end='')

    print()

print()

for i in range(rows):
    # print(i, end='\t')
    for j in range(cols):
        if (i == 0 or j == 0 or i == rows-1 or j == cols-1
        or i == j or i == cols - j -1 or i == rows // 2 or j == cols):
            print('* ', end='')
        else:
            print('  ', end='')

    print()

print()
