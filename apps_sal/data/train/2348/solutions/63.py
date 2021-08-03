from bisect import*
r = range
n, *t = map(int, open(0).read().split())
x = t[:n]
d = [[bisect(x, y + t[n]) - 1for y in x]] + [[0] * n for _ in r(16)]
for i in r(16):
    for j in r(n):
        d[i + 1][j] = d[i][d[i][j]]
for a in zip(t[n + 2::2], t[n + 3::2]):
    a, b = sorted(i - 1for i in a)
    c = 1
    for i in r(16, -1, -1):
        if d[i][a] < b:
            a = d[i][a]
            c += 2**i
    print(c)
