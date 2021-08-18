from math import gcd
from functools import reduce


def func(W, i, g, dp):
    if i >= len(W):
        return 0
    if dp[i][g] != -1:
        return dp[i][g]
    _g = gcd(g, W[i])
    ans1 = 1 + func(W, i + 1, _g, dp) if _g == 1 else func(W, i + 1, _g, dp)
    dp[i][g] = ans1 + func(W, i + 1, g, dp)
    return dp[i][g]


result = ""
for _ in range(int(input())):
    n = int(input())
    W = [int(x) for x in input().split()]
    dp = [[-1 for x in range(10000 + 3)] for y in range(70)]

    t = func(W, 0, 0, dp)
    result += str(t) + "\n"
print(result[:-1])
