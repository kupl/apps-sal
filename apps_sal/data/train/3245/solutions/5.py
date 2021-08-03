from math import factorial as fact


def checkchoose(m, n):
    l = [i for i in range(1, n + 1) if fact(n) / (fact(i) * fact(n - i)) == m]
    return 0 if m < n else l[0] if l else -1
