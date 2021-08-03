val = int(input())
for i in range(val):
    n = int(input())

    p = list(input())
    for j in range(0, n, 2):
        p[j] = chr(122 - (ord(p[j]) - 97))

        if j % 2 == 0 and j + 1 < n:
            p[j + 1] = chr(122 - (ord(p[j + 1]) - 97))
            p[j], p[j + 1] = p[j + 1], p[j]

    print(''.join(p))
