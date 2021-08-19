from math import gcd
from functools import reduce
# aa = []


def func(W, i, g, dp):
    # print(i,g)
    # aa.append(1)
    if i >= len(W):
        return 0
    if dp[i][g] != -1:
        return dp[i][g]
    _g = gcd(g, W[i])
    ans1 = 1 + func(W, i + 1, _g, dp) if _g == 1 else func(W, i + 1, _g, dp)
    dp[i][g] = ans1 + func(W, i + 1, g, dp)
    return dp[i][g]

    # return ans1 + func(W,i+1,g,dp)
result = ""
for _ in range(int(input())):
    n = int(input())
    W = [int(x) for x in input().split()]
    dp = [[-1 for x in range(10000 + 3)] for y in range(70)]

    # aa=[]

    t = func(W, 0, 0, dp)
    # print(t,len(aa))
    result += str(t) + "\n"
print(result[:-1])
# submitted 03:05
