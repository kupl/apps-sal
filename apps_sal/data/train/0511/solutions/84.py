import sys
from collections import deque, defaultdict, Counter
from itertools import accumulate, product, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from math import ceil, floor, sqrt, gcd, inf
from copy import deepcopy
import numpy as np
import scipy as sp
INF = inf
MOD = 1000000007
n = int(input())
A = [int(i) for i in input().split()]
tmp = A[0]
res = 0
for i in range(1, n):
    tmp ^= A[i]
res = [tmp ^ A[i] for i in range(n)]
res = ' '.join([str(r) for r in res])
print(res)
