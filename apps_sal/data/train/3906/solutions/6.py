from math import factorial as fac


def C(n, k):
    return fac(n) // (fac(k) * fac(n - k))


def total(arr):
    l = len(arr)
    return sum(arr[i] * C(l - 1, i) for i in range(l))
