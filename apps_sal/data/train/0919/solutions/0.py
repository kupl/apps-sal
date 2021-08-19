"""Author- Akshit Monga"""
from sys import stdin, stdout
input = stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    dp = [-1 for i in range(0, n + 1)]
    for i in a:
        var1 = dp[i]
        var2 = ans
        ans = max(ans, var1 + 1)
        dp[i] = max(dp[i], var2 + 1)
    print(n - ans)
