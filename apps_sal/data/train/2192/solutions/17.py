from bisect import bisect_left, bisect_right
from collections import Counter
from collections import deque
from itertools import accumulate

import math

R = lambda: map(int, input().split())
n = int(input())
a, dp = sorted([tuple(R()) for _ in range(n)]), [0] * n
for i, (loc, dis) in enumerate(a):
    dp[i] = dp[bisect_left(a, (loc - dis, -10**10)) - 1] + 1
print(n - max(dp))
