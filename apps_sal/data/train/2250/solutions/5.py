from sys import *
def f(): return map(int, stdin.readline().split())


n, m, k = f()
w, h = 2 * n, 2 * m

inf = 1e11
s = [inf] * (w + h)
a = b = t = 0

while 1:
    if s[b - a] == inf:
        s[b - a] = t - a
    d = min(w - a, h - b)
    t += d
    a = (a + d) % w
    b = (b + d) % h
    if a % n == b % m:
        break

for i in range(k):
    x, y = f()
    q = min(s[b - a] + a for a in (x, w - x) for b in (y, h - y))
    print(q if q < inf else -1)
