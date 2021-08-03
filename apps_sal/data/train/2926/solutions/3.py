from itertools import islice


def reverse(a):
    cs = (c for s in reversed(a) for c in reversed(s))
    return [''.join(islice(cs, 0, len(s))) for s in a]
