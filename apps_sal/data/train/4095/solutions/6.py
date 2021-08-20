from collections import Counter


def added_char(*args):
    (c1, c2) = map(Counter, args)
    return (c2 - c1).popitem()[0]
