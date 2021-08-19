from sys import stdin, stdout, maxsize
from math import sqrt, log, factorial, gcd
from collections import defaultdict as D
from bisect import insort
for _ in range(int(input())):
    n = int(input()) - 1
    for i in range(n, -1, -1):
        for j in range(n - i, 0, -1):
            print(j, end='')
        for j in range(i + 1):
            print(j, end='')
        print()
