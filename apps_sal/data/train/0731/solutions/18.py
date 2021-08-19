try:
    MAX = 10 ** 9
    (a, b) = list(map(int, input().split()))
    c = []
    for i in range(a):
        c.append([-1 for j in range(a)])
    for j in range(b):
        (d, e, p) = [int(i) for i in input().split()]
        c[d - 1][e - 1] = p
        c[e - 1][d - 1] = p
    for i in range(a):
        for j in range(a):
            if i == j:
                c[i][j] = 0
            elif c[i][j] == -1:
                c[i][j] = MAX
    for k in range(a):
        for i in range(a):
            for j in range(a):
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])
    p = 0
    for i in range(a):
        for j in range(a):
            p = max(c[i][j], p)
    print(p)
except Exception:
    pass
