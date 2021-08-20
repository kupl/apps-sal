def ss(a):
    return sum([e * e for e in a])


def sc(b):
    return sum([e * e * e for e in b])


def array_madness(a, b):
    return ss(a) > sc(b)
