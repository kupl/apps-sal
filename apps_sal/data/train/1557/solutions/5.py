t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    r = input()
    c0 = 0
    c1 = 0
    d0 = 0
    d1 = 0
    for i in s:
        if i == '1':
            c1 = c1 + 1
        else:
            c0 = c0 + 1
    for i in r:
        if i == '1':
            d1 = d1 + 1
        else:
            d0 = d0 + 1
    if ((c0 == d0) and (c1 == d1)):
        print('YES')
    else:
        print('NO')
