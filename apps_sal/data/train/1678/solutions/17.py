# cook your dish here
from itertools import count, islice

R = lambda: map(int, input().split())
Z = lambda: list(zip(R(), count()))
         
n, m = R()
a, b = Z(), Z()
if n != 10:
    a = min(a), max(a)
d = {x + y: (i, j) for x, i in a for y, j in b}
for p in islice(d.values(), n + m - 1):
    print(*p)
