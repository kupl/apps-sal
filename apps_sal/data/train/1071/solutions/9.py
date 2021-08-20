from sys import stdin, stdout, maxsize
from math import sqrt, log, factorial, gcd
from collections import defaultdict as D
from bisect import insort
for _ in range(int(input())):
    (x, q) = map(int, input().split())
    b = list(bin(x))
    b = b[2:]
    b = b[::-1]
    b.insert(0, '0')
    d = D(lambda: 0)
    l = len(b)
    for i in range(l):
        d[i] = b[i]
    for i in range(q):
        t = int(input())
        if t <= 3:
            x = int(input())
            if t == 1:
                if d[x] == '1':
                    print('ON')
                else:
                    print('OFF')
            elif t == 2:
                d[x] = '1'
            else:
                d[x] = '0'
        else:
            (p, q) = map(int, input().split())
            (d[p], d[q]) = (d[q], d[p])
