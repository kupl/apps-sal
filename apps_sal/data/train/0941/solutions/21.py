for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    c = []
    d = []
    p, q = 0, 0
    x, y = 0, 0
    for i in range(1, a + 1):
        c.append(i)
    for i in range(1, b + 1):
        d.append(i)
    for i in range(len(c)):
        if(c[i] % 2 == 0):
            p += 1
        else:
            q += 1
    for i in range(len(d)):
        if(d[i] % 2 == 0):
            x += 1
        else:
            y += 1
    print(p * x + q * y)
