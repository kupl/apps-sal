from itertools import chain, zip_longest


def interweave(s1, s2):
    L = chain.from_iterable(zip_longest(s1, s2, fillvalue=''))
    return ''.join((c for c in L if not c.isdigit()))
