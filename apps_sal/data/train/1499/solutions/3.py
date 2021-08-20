from sys import *
input = stdin.readline
for u in range(int(input())):
    (n, m) = list(map(int, input().split()))
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    s = input()
    (x, y) = list(map(int, input().split()))
    d = [0] * len(s)
    k = [0] * len(s)
    for i in range(n):
        for j in range(m):
            if str(l[i][j]) != s[(i + j) % (n + m - 1)]:
                d[(i + j) % (n + m - 1)] += 1
            k[i + j] += 1
    c = 0
    for i in range(len(s)):
        c += min(d[i] * x, y + (k[i] - d[i]) * x)
    print(c)
