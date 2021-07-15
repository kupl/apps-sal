def max_gap(lst):
    lst.sort()
    return max(y - x for x, y in zip(lst, lst[1:]))
