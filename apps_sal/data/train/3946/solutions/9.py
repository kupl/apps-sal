from itertools import chain, zip_longest


def interweave(s1, s2):
    return ''.join([c for c in chain.from_iterable(zip_longest(s1, s2)) if c and (not c.isdigit())])
