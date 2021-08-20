import math


def predict(candidates, polls):
    t = {}
    for (i, j) in enumerate(candidates):
        m = 0
        n = 0
        for z in polls:
            n += z[1]
            m += z[0][i] * z[1]
        t[j] = round1(m / n)
    return t
