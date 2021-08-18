
from sys import stdin, stdout
mod = 10**9 + 7
store = dict()


def power10(N):
    x = bin(N)
    i = -1
    tmp = 10
    r = 1
    while x[i] != 'b':
        if x[i] == '1':
            r *= tmp
            r %= mod
        tmp = (tmp % mod) * (tmp % mod)
        tmp %= mod
        i -= 1
    return r % mod


T = int(input().strip())

for _ in range(T):
    N, W = map(int, input().strip().split())
    dp = [-1] * (N + 1)
    dp[0] = 1
    if W > 8 or W < -9:
        print(0)
    else:
        if W >= 0:
            if store.get(N - 2) == None:
                store[N - 2] = power10(N - 2)
            res = (9 - W) * store[N - 2]
        else:
            if store.get(N - 2) == None:
                store[N - 2] = power10(N - 2)
            res = (W + 10) * store[N - 2]
        print(res % mod)
