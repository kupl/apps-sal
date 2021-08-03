for __ in range(int(input())):
    n, m = map(int, input().split())
    g = [[]for _ in range(n + 1)]
    long = []
    di = {}
    stable = [0 for _ in range(n + 1)]
    edges = [0 for _ in range(m)]
    for i in range(m):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
        stable[y] += 1
        long.append([x, y])
        di[(x, y)] = i
        di[(y, x)] = i
    f = 1
    if m % 2:
        f = 0
    for i in range(m):
        c, d = long[i][0], long[i][1]
        if stable[c] % 2 == 1 and stable[d] % 2 == 1:
            stable[c] += 1
            stable[d] -= 1
            edges[i] = 1
    s = []
    for i in range(1, n + 1):
        if stable[i] % 2 == 1:
            s.append(i)
    while s and f:
        set1 = set()
        for i in s:
            if stable[i] % 2:
                y = g[i][0]
                w = di[(i, y)]
                stable[y] += 1
                stable[i] -= 1

                set1.add(y)
                edges[w] = abs(edges[w] - 1)
        s = set1
    if(f):
        print(*edges)
    else:
        print(-1)
