def twos_difference(lst):
    s = set(lst)
    return [(n, n+2) for n in sorted(s) if n+2 in s]
