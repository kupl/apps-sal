from itertools import cycle


def calc(lst):
    return sum(((a ** 2 if a > 0 else a) * b * c for (a, b, c) in zip(lst, cycle((1, 1, 3)), cycle((1, 1, 1, 1, -1)))))
