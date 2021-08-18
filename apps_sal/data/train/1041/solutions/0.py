for u in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = []
    dd = []
    s = 1
    for i in range(n - 1):
        s = l[i]
        d.append(s)
        dd.append([i, i])
        for j in range(i + 1, n):
            s = s * l[j]
            d.append(s)
            dd.append([i, j])
    d.append(l[n - 1])
    dd.append([n - 1, n - 1])
    k = len(d)
    m = max(d)
    x, y = 0, 0
    for i in range(k):
        if(d[i] == m):
            x = dd[i]
    print(m, *x)
