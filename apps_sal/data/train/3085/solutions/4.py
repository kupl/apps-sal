from math import factorial


def aks_test(p):
    if p in (1, 2):
        return p == 2
    f = p
    for k in range(1, 1 + p // 2):
        if f % p:
            return False
        f *= p - k
        f //= k + 1
    return True
