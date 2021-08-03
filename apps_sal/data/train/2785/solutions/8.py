import math


def parameter(n):

    d = [int(x) for x in str(n)]

    s = sum(d)

    p = 1

    for i in range(0, len(d)):

        p *= d[i]

    g = math.gcd(s, p)

    l = (s * p) // g

    return l
