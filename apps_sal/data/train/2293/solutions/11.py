from itertools import accumulate
import sys
input = sys.stdin.readline


def merge(x, y):
    a, b = dp[x]
    c, d = dp[y]
    if a >= c:
        return (a, max(c, b))
    return (c, max(a, d))


n = int(input())
A = tuple(map(int, input().split()))
dp = [(a, 0) for a in A]
for j in range(n):
    for i in range(1 << n):
        if i & (1 << j):
            dp[i] = merge(i, i & ~(1 << j))
L = tuple(accumulate((sum(d) for d in dp), max))
print(*L[1:], sep="\n")
