from statistics import mean


def array_center(a):
    (n, m) = (min(a), mean(a))
    return [x for x in a if abs(x - m) < n]
