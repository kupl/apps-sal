from functools import reduce


def colorful(n):
    ld = [int(d) for d in str(n)]
    l = len(ld)
    p = [reduce(int.__mul__, ld[i:i + k]) for k in range(1, l + 1) for i in range(l - k + 1)]
    return len(p) == len(set(p))
