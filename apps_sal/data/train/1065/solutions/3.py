from math import *
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(input())

    l = []
    for i in range(n):
        for j in range(m):
            if(a[i][j] == '1'):
                l.append((i, j))
    d = {}
    for i in range(1, n + m - 2 + 1):
        d[i] = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            dis = abs(l[i][0] - l[j][0]) + abs(l[i][1] - l[j][1])
            d[dis] += 1
    for i in range(1, n + m - 2 + 1):
        print(d[i], end=' ')
