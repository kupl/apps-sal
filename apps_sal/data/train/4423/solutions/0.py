from collections import Counter as C


def ball_probability(b):
    d, n, p = C(b[0]), len(b[0]), 1
    for i in b[1]:
        p *= d.get(i, 0) / n
        n -= b[2] ^ 1
        d[i] -= b[2] ^ 1
    return round(p, 3)
