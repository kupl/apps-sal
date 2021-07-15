from math import factorial


def permutation_average(n):
    m = len(str(n))
    s = sum(map(int, str(n)))
    return round(sum(s * 10 ** i for i in range(m)) / float(m))
