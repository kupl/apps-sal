import math
import bisect


def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x) % p
        y = y >> 1  # y = y/2
        x = (x * x) % p
    return res


def inn():
    return int(input())


def inl():
    return list(map(int, input().split()))


MOD = 10**9 + 7
INF = inf = 10**18 + 5

for t in range(int(input())):
    n, k = inl()

    if n >= k or k < 3:
        print(k - 1)
        continue

    a = k - 1
    d = n - 1
    m = a // d + 1
    ans = ((m * (2 * a - (m - 1) * d)) // 2) % MOD
    print(ans)
