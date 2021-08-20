import sys
from collections import defaultdict
from copy import copy
MOD = 10 ** 9 + 7


def R(t=int):
    return t(input())


def RL(t=int):
    return [t(x) for x in input().split()]


def RLL(n, t=int):
    return [RL(t) for _ in range(n)]


def primes(n):
    P = []
    n = int(n)
    U = [1] * (n + 1)
    p = 2
    while p <= n:
        if U[p]:
            P += [p]
            x = p
            while x <= n:
                U[x] = 0
                x += p
        p += 1
    return P


def solve():
    S = R(str).strip()
    X = [ord(c) - ord('a') for c in S]
    P = primes(10000)
    L = defaultdict(lambda: 0)
    s = 0
    for i in range(len(S)):
        p = i in P
        NL = defaultdict(lambda: 0)
        for a in range(26):
            for l in L:
                NL[l + a * p] += L[l]
        for a in range(X[i]):
            NL[s + a * p] += 1
        s += X[i] * p
        L = NL
    L[s] += 1
    r = 0
    for p in P:
        r += L[p]
    print(r % MOD)


T = R()
for t in range(1, T + 1):
    solve()
