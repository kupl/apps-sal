def twos_difference(lst):
    return [(i, i + 2) for i in sorted(lst) if i + 2 in lst]
