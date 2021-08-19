import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)


def ii(): return int(input())
def si(): return input()


def jn(x, l): return x.join(map(str, l))
def sl(): return list(map(str, input().strip()))
def mi(): return list(map(int, input().split()))
def mif(): return list(map(float, input().split()))
def lii(): return list(map(int, input().split()))


def ceil(x): return int(x) if(x == int(x)) else int(x) + 1


def ceildiv(x, d): return x // d if(x % d == 0) else x // d + 1


def flush(): return stdout.flush()
def stdstr(): return stdin.readline()
def stdint(): return int(stdin.readline())
def stdpr(x): return stdout.write(str(x))


mod = 1000000007


def sol(s):
    dp = [0] * (len(s) + 2)
    dp[0] = 1

    for i in range(len(s)):
        if int(s[i]) != 0:
            dp[i + 1] += dp[i]

        if int(s[i:i + 2]) >= 10 and int(s[i:i + 2]) <= 26:
            dp[i + 2] += dp[i]

    return dp[len(s)]


# main code
for _ in range(ii()):
    s = si()
    ans = sol(s)
    print(ans % mod)
