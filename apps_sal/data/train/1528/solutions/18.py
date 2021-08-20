a = int(input())
for i in range(a):
    b = str(input()).split(' ')
    c = str(input()).split(' ')
    li = []
    n = 0
    for i1 in range(int(b[1])):
        li.append(c[int(b[0]) - i1 - 1])
    for i2 in range(int(b[1]) - 1):
        if li[i2 + 1] != li[i2]:
            n += 1
    if c[int(b[0]) - 1] == 'H':
        n += 1
    if n % 2 == 0:
        print(c[:int(b[0]) - int(b[1])].count('H'))
    else:
        print(c[:int(b[0]) - int(b[1])].count('T'))
