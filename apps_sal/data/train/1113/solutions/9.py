#!/usr/bin/env python

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    D = {}
    for e in A:
        D[e] = D.get(e, 0) + 1
    C = max(D.values())
    V = min([e[0] for e in [e for e in list(D.items()) if e[1] == C]])
    print(V, C)
