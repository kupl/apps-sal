from sys import stdin


def sin():
    return stdin.readline()


for _ in range(int(sin())):
    n, m = map(int, sin().split())
    l = list(map(int, sin().split(" ")))
    g = [0] * max(l) * 2
    for i in l:
        g[i - 1] = 1
    p = g.index(0) + 1
    if p == m:
        print(n)
    elif p < m:
        print(-1)
    else:
        print(n - l.count(m))
