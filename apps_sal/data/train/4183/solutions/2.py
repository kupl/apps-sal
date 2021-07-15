def greatest_distance(lst):
    return max((distance(lst, n) for n in set(lst) if lst.count(n) > 1), default=0)


def distance(lst, item):
    return len(lst) - 1 - lst[::-1].index(item) - lst.index(item)

