from math import gcd


def gcd_matrix(a, b):
    k = a[:]
    p = 0
    for i in range(len(b)):
        s = []
        for j in range(len(a)):
            k[j] = gcd(a[j], b[i])
            s.append(k[j])
        p += sum(s)
    return round(p / (len(a) * len(b)), 3)
