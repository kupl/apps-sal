from itertools import cycle


def thirt(n):
    c = cycle([1, 10, 9, 12, 3, 4])
    m = sum(int(l) * next(c) for l in str(n)[::-1])
    return m if m == n else thirt(m)
