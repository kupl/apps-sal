from collections import deque


def rollingmax(x, y, r, a):
    k = 2 * r + 1
    d = deque()
    lx = len(x)
    for i in range(lx + r):
        if i < lx:
            while d and d[-1][1] <= x[i]:
                d.pop()
            d.append((i, x[i]))
        while d and d[0][0] <= i - k:
            d.popleft()
        if i >= r:
            y[i - r] = d[0][1] - abs(i - r - a)


n, m, d = [int(x) for x in input().split()]
a, ball, t0 = [int(x) for x in input().split()]
f = [-abs(i - a) for i in range(1, n + 1)]
g = [0] * n
for _ in range(m - 1):
    a, b, t = [int(x) for x in input().split()]
    ball += b
    r = min(n - 1, (t - t0) * d)
    t0 = t
    rollingmax(f, g, r, a - 1)
    f, g = g, f

print(max(f) + ball)
