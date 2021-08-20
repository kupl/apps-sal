import math
import functools


def survivor(zombies):
    zombies.sort()
    if not zombies:
        return -1
    divisor = functools.reduce(math.gcd, zombies)
    if divisor > 1:
        return -1
    A = zombies
    Q = [0]
    P = [len(zombies)] + [None] * (A[0] - 1)
    S = [0]
    a = [A[0] * A[len(A) - 1]] * (A[0] - 1)
    S = S + a
    Amod = list(map(lambda x: x % A[0], A))
    while len(Q) > 0:
        v = Q[0]
        Q.pop(0)
        for j in range(2, P[v] + 1):
            u = v + Amod[j - 1]
            if u >= A[0]:
                u = u - A[0]
            w = S[v] + A[j - 1]
            if w < S[u]:
                S[u] = w
                P[u] = j
                if u not in Q:
                    Q.append(u)
    if int(max(S)) - A[0] < 0:
        return 0
    return int(max(S)) - A[0]
