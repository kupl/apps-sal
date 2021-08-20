from sys import stdin
import functools


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


MAX = 10001


def func(ind, g, dp, n, a):
    if ind == n:
        if g == 1:
            return 1
        else:
            return 0
    if dp[ind][g] != -1:
        return dp[ind][g]
    ans = func(ind + 1, g, dp, n, a) + func(ind + 1, gcd(a[ind], g), dp, n, a)
    dp[ind][g] = ans
    return dp[ind][g]


def countSubsequences(a, n):
    dp = [[-1 for i in range(MAX)] for i in range(n)]
    count = 0
    for i in range(n):
        count += func(i + 1, a[i], dp, n, a)
    return count


tc = int(stdin.readline())
for i in range(tc):
    n = int(stdin.readline())
    list1 = list(map(int, stdin.readline().split()))
    print(countSubsequences(list1, n))
