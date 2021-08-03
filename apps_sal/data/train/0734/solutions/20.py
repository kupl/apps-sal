for _ in range(int(input())):
    n = int(input())
    d = {}
    b = [0] * n
    g = {}
    h = {}
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
            h[a[i]].append(i)
        else:
            d[a[i]] = 1
            h[a[i]] = [i]
    x = list(map(list, sorted(list(d.items()), key=lambda y: y[1])))
    # print(x)
    l = 0
    r = len(x) - 1

    for i in d:
        g[i] = []

    while l < r:
        if x[r][1] >= x[l][1]:
            g[x[r][0]].append([x[l][0], x[l][1]])
            g[x[l][0]].append([x[r][0], x[l][1]])
            x[r][1] -= x[l][1]
            x[l][1] = 0
            l += 1
        else:
            if x[r][1] > 0:
                g[x[r][0]].append([x[l][0], x[r][1]])
                g[x[l][0]].append([x[r][0], x[r][1]])
                x[l][1] -= x[r][1]
                x[r][1] = 0
            r -= 1
    # print(g)
    s = []
    m = x[-1][0]
    k = -1
    for i in range(n):
        if g[a[i]] != []:
            b[i] = g[a[i]][-1][0]
            g[a[i]][-1][1] -= 1
            if g[a[i]][-1][1] == 0:
                g[a[i]].pop()
        else:
            s.append(i)
            k = a[i]
    # print(b)
    if k == m:
        print('No')
    else:
        for i in h[m]:
            if b[i] != k:
                if s != []:
                    b[s.pop()] = b[i]
                    b[i] = k
        print('Yes')
        print(*b)
