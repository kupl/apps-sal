from itertools import accumulate


def luxhouse(houses):
    return [max(0, y - x + 1) for (x, y) in zip(houses[::-1], accumulate([0] + houses[:0:-1], max))][::-1]
