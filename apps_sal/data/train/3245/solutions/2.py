from math import factorial as fact


def checkchoose(m, n):
    for k in range(0, (n) // 2 + 1):
        if fact(n) // (fact(n - k) * fact(k)) == m:
            return k
    return -1
