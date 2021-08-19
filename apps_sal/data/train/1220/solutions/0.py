import sys
from collections import defaultdict
from copy import copy


def R(t=int):
    return t(eval(input()))


def RL(t=int):
    return [t(x) for x in input().split()]


def RLL(n, t=int):
    return [RL(t) for _ in range(n)]


def solve():
    (N, Q) = RL()
    P = RL()
    B = RL()
    phones = sorted(zip(P, B))
    S = defaultdict(lambda: [])
    for (p, b) in phones:
        for i in range(2 ** 7):
            if i >> b & 1:
                S[i] += [p]
    B = set(B)
    I = [0] * len(B)
    for _ in range(Q):
        (b, K) = RL()
        s = RL()
        x = 0
        for b in s:
            x += 1 << b
        if len(S[x]) < K:
            print(-1)
        else:
            print(S[x][-K])


T = 1
for t in range(1, T + 1):
    solve()
