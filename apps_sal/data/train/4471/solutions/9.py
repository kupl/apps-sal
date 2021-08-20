from itertools import cycle


def lamps(a):
    return min(sum((x != y for (x, y) in zip(a, cycle([0, 1])))), sum((x != y for (x, y) in zip(a, cycle([1, 0])))))
