
t = int(input())
while t:
    n, c = map(int, input().split())
    u = c
    a = []
    d = {}
    for i in range(n):
        p, q = map(int, input().split())
        a += [[p, q]]
        x = min(p, q)
        d[p - q] = []

    for i in range(n):
        y, z = a[i][0], a[i][1]
        m = y - z
        d[m].append(a[i][0])
    # print(d)
    e = []
    for i in d.values():
        e.append(i)
    # print(a)
    # print(e)
    g = []
    for k in e:
        d = {}
        for i in range(len(k)):
            d[k[i] % c] = []
        for i in range(len(k)):
            d[k[i] % c].append(k[i])
        for i in d.values():
            g.append(i)
        # print(g)

    c = 0
    print(len(g), end=" ")
    for i in range(len(g)):
        # print(1)
        g[i].sort()
        med = len(g[i]) // 2
        for j in range(len(g[i])):
            c += abs(g[i][j] - g[i][med]) // u
    print(c)

    t -= 1
