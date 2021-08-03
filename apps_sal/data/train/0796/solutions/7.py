import sys


def altmem(a, b):
    if a < 0 and b >= 0:
        return True
    if a >= 0 and b < 0:
        return True
    return False


for __ in range(eval(input())):
    n = eval(input())
    lists = list(map(int, sys.stdin.readline().split()))
    dp = [0] * (100010)
    dp[n - 1] = 1
    for i in range(n - 2, -1, -1):
        dp[i] = dp[i + 1] + 1 if altmem(lists[i], lists[i + 1]) else 1
    print(" ".join(str(i) for i in dp[:n]))
