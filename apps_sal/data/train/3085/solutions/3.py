P = [2] + [p for p in range(3, 500000, 2) if all(p % v for v in range(3, int(p**.5 + 1), 2))]
S = set(P)


def aks_test(p):
    return p in S or p > 2 and p & 1 and all(p % v for v in P)
