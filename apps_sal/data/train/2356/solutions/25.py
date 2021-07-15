import sys
import math
import itertools
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush
from operator import itemgetter, attrgetter
from itertools import permutations, combinations
sys.setrecursionlimit(500000)

n, K = map(int, input().split())
mo = 998244353
a = [[0] * (n + 2) for _ in range(n + 2)]
a[0][0] = 1
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        a[i][j] = a[i - 1][j - 1] + (a[i][j * 2] if j * 2 <= n else 0)
        a[i][j] %= mo
print(a[n][K] % mo)
