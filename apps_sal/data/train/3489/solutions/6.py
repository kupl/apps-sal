from itertools import accumulate


def save(sizes, hd):
    i = 0
    for i, acc in enumerate(accumulate(sizes), 1):
        if acc > hd:
            return i - 1
    return i
