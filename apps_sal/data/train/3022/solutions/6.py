def two_highest(l):
    return isinstance(l, list) and sorted(set(l))[-2:][::-1]
