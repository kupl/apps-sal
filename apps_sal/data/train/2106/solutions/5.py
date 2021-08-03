import sys
from functools import reduce

for n in sys.stdin:
    n = int(n)
    cards = [list(map(int, input().split()[1:])) for i in range(n)]
    mid = []
    a, b = 0, 0
    def add(x=0, y=0): return x + y
    for c in cards:
        s = len(c)
        m = s >> 1
        a += reduce(add, c[:m] or [0])
        b += reduce(add, c[m + (s & 1):] or [0])
        if s & 1 == 1:
            mid.append(c[m])
    mid.sort(reverse=True)
    j = True
    for c in mid:
        if j:
            a += c
        else:
            b += c
        j = not j
    print(a, b)
