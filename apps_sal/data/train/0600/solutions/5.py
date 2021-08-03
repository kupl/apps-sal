import math


def fib(n):
    if n < 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10
    # print(n, dp)
    return dp[n]


t = int(input())

for _ in range(t):
    n = int(input())
    exp = int(math.floor(math.log(n, 2)))
    arg = (2**exp - 1) % 60

    print(fib(arg))
