from functools import reduce


def closest(arr):
    return (lambda r: None if r[1] else r[0])(reduce(lambda a, b: [a[0], True] if a[0] and a[0] == -b else [b, False] if abs(b) < abs(a[0]) else a, arr, [999999, False]))
