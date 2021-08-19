t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    for j in range(2, n, 2):
        if int((n ** 2 - j ** 2) ** 0.5) == (n ** 2 - j ** 2) ** 0.5:
            c = c or 1
            break
        else:
            c = c or 0
    if c == 1:
        print('YES')
    else:
        print('NO')
