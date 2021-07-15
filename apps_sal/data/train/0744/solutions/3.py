from sys import stdin, stdout, maxsize
from math import sqrt, log, factorial, gcd
from collections import defaultdict as D
from bisect import insort

for _ in range(int(input())):
    n = int(input())
    l = []
    factor = 0
    for i in range(1, (n // 2) + 2):
        if i == 1:
            l.append('*')
        else:
            l.append('*' + factor * ' ' + '*')
            factor += 1
    for i in l: print(i)
    for i in range(len(l) - 2, -1, -1):
        print(l[i])
