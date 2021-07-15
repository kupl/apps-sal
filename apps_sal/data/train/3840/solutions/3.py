from collections import defaultdict
from bisect import bisect

a, memo = 2, defaultdict(int)
for a in range(2, 1001):
    x = a**2
    while x <= 1000000:
        memo[x] += 1
        x *= a
memo = sorted(memo.items())

def largest_power(n):
    if n <= 4: return n>1, -1
    return memo[bisect(memo, (n,))-1]
