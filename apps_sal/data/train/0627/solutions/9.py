import sys
from collections import defaultdict
sys.setrecursionlimit(3000)


def R(t=int): return t(eval(input()))
def RL(t=int): return [t(x) for x in input().split()]
def RLL(n, t=int): return [RL(t) for _ in range(n)]


MOD = 10**9 + 7


def divc(x):
    return pow(x, MOD - 2, MOD)


def C(n, k):
    r = 1
    for i in range(k + 1, n + 1):
        r = r * i % MOD
    t = 1
    for i in range(1, n - k + 1):
        t = t * i % MOD
    return r * divc(t) % MOD


def solve():
    N, K = RL()
    print(C(K + N - 1, N - 1))


T = 1
for t in range(1, T + 1):
    solve()
