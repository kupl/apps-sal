from collections import Counter as C


def solve(Q, S):
    (Q, S) = (C(Q), C(S))
    if all((V in Q and S[V] <= Q[V] for V in S)):
        return sum((Q[V] - (S[V] if V in S else 0) for V in Q))
    return 0
