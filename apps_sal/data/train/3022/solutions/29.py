def two_highest(l):
    return isinstance(l, list) and sorted(set(l), key=lambda x: -x)[:2]
