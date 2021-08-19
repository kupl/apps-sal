from sys import stdin, stdout
from math import gcd, log2, log10, floor
import math
from collections import defaultdict, OrderedDict
from bisect import bisect_left
(n, k, p) = [int(i) for i in input().split()]
a = list(map(int, input().split()))
asort = a[:]
asort.sort()
dict = defaultdict(int)
theta = 1
dict[asort[0]] = 1
for i in range(1, n):
    if asort[i] - asort[i - 1] <= k:
        dict[asort[i]] = theta
    else:
        theta += 1
        dict[asort[i]] = theta
for i in range(p):
    (alpha, beta) = list(map(int, input().split()))
    alpha -= 1
    beta -= 1
    if dict[a[alpha]] == dict[a[beta]]:
        print('Yes')
    else:
        print('No')
