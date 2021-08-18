import sys
from math import log2
from itertools import combinations


for _ in range(int(sys.stdin.readline())):
    n, m = list(map(int, sys.stdin.readline().split()))
    a = set(map(int, sys.stdin.readline().split()))
    b = set(map(int, sys.stdin.readline().split()))
    c = []
    for i in a:
        if i not in b:
            c.append(i)
    for i in b:
        if i not in a:
            c.append(i)
    c = list(set(c))
    c.sort()
    print(*c)
