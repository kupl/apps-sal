import sys
import math
from collections import defaultdict, Counter
t = int(input())
for i in range(t):
    (a, m) = map(int, input().split())
    r = (m - 1) // a
    l = []
    for j in range(1, r + 1):
        if m % (a * j + 1) == 0:
            d = m // (a * j + 1)
            l.append(d * j)
    print(len(l))
    print(*l)
