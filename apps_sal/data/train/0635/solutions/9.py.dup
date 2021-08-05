# cook your dish here
from sys import stdin, stdout
import math
from itertools import permutations, combinations
from collections import defaultdict
from bisect import bisect_left
from bisect import bisect_right


def L():
    return list(map(int, stdin.readline().split()))


def In():
    return list(map(int, stdin.readline().split()))


def I():
    return int(stdin.readline())


P = 1000000007


def main():
    n, k = In()
    arr = L()
    ans = 0
    dict1 = {}

    for i in range(n):
        if arr[i] in list(dict1.keys()):
            dict1[arr[i]] += 1
        else:
            dict1[arr[i]] = 1
    l1 = [-1] + list(dict1.keys())
    v = min(k, len(l1))
    dp = [[0 for i in range(v + 1)]for i in range(len(l1))]
    dp[0][0] = 1
    for i in range(1, len(l1)):
        dp[i][0] = 1
        for j in range(1, v + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * dict1[l1[i]]
    for i in range(k + 1):
        ans += dp[len(l1) - 1][i]
        ans = ans % P
    print(ans)


def __starting_point():
    main()


__starting_point()
