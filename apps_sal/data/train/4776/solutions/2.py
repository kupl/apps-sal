(S, C) = ([1, 1], [0, 0])


def length_sup_u_k(n, k):
    return update(n) or sum((v >= k for v in S[:n]))


def comp(n):
    return update(n) or C[n - 1]


def update(n):
    for _ in range(n + 1 - len(S)):
        S.append(S[-S[-2]] + S[-S[-1]])
        C.append(C[-1] + (S[-2] > S[-1]))
