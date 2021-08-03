def twos_difference(l):
    r = [(i, i + 2) for i in sorted(l) if i + 2 in l]
    return r


def twos_difference(l): return [(i, i + 2) for i in sorted(l) if i + 2 in l]
