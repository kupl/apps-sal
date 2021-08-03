from math import *
from collections import *
from itertools import *
from functools import *
from bisect import *
from heapq import *
from operator import *
from sys import *
setrecursionlimit(100000000)

n, k = map(int, input().split())
l = list(map(int, input().split()))
l.append(reduce(xor, l))
l = list(accumulate(l, xor))
for _ in range(k):
    v = int(input())
    print(l[(v - 1) % len(l)])
