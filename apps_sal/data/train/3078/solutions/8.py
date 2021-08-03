from numpy import mean


def array_center(arr):
    m, a = min(arr), mean(arr)
    return list(filter(lambda n: abs(n - a) < m, arr))
