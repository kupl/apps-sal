def H(Q):
    (D, S) = (0, len(Q))
    for V in Q:
        if list == type(V):
            (d, s) = H(V)
            (D, S) = (max(d, D), max(s, S))
    return (1 + D, S)


def W(Q, R, D, S):
    Q = Q + [R] * (S - len(Q))
    return [W(V if list == type(V) else [V] * S, R, D - 1, S) for V in Q] if D - 1 else Q


def normalize(Q, R=0):
    return W(Q, R, *H(Q))
