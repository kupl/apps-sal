# cook your dish here
from math import floor, sqrt
try:
    long
except NameError:
    long = int


def fac(n):
    step, maxq, d = lambda x: 1 + (x << 2) - ((x >> 1) << 1), long(floor(sqrt(n))), 1
    q = n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + fac(n // q) or [n]


n, k, s = map(int, input().split())
a, di, l, m, ans, su = list(map(int, input().split())), {}, [], 0, 0, 0
for i in a:
    bb, su = list(set(fac(i))), su + i
    for j in bb:
        try:
            di[j] += 1
        except KeyError:
            m, di[j] = m + 1, 1
    l.append(su * (k - m * s))
    if su * (k - m * s) < 0:
        m, di, su = 0, {}, 0
print(max(l))
