from itertools import cycle


def buy_newspaper(s1, s2):
    if set(s2) - set(s1):
        return -1
    c, n = cycle(s1), 0
    for c2 in s2:
        while True:
            n, c1 = n + 1, next(c)
            if c1 == c2:
                break
    return n // len(s1) + (n % len(s1) != 0)
