from sys import stdin, stdout, maxsize
from math import sqrt, log, factorial, gcd
from collections import defaultdict as D
from bisect import insort

for _ in range(int(input())):
    n = bin(int(input()))
    print(n.count("1"))
