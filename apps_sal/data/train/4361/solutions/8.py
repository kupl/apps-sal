M, U = {}, []


def H(Q):
    R = 0
    while Q:
        if Q % 10 < 1:
            return 0
        R += 1 << (Q % 10 * 3)
        Q //= 10
    return R


for F in range(1, 10000):
    F = F * F
    R = H(F)
    if R:
        U.append(F)
        M.setdefault(R, []).append(F)


def next_perfectsq_perm(Q, S):
    for V in U:
        if Q < V:
            T = M.get(H(V))
            if T and S == len(T):
                return T[-1]
