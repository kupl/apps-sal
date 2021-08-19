import math
import sys
from bisect import bisect_right, bisect_left, insort_right
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import accumulate, permutations, combinations
from sys import stdout


def R():
    return map(int, input().split())


n = int(input())
dp = defaultdict(lambda: [0, 0])
dp[0] = [1, 0]
xor = res = 0
for (i, x) in enumerate(R()):
    xor ^= x
    res += dp[xor][i + 1 & 1]
    dp[xor][i + 1 & 1] += 1
print(res)
