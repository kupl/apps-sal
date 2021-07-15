def comp(a1, a2):
    return isinstance(a1, list) and isinstance(a2, list) and sorted(x*x for x in a1) == sorted(a2)
