from operator import itemgetter


def min_and_max(l, d, x):
    return list(itemgetter(0, -1)([i for i in range(l, d + 1) if sum(map(int, list(str(i)))) == x]))
