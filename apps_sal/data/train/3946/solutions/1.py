from itertools import chain, zip_longest
def interweave(s1, s2):
    return ''.join(char for char in chain.from_iterable(zip_longest(s1, s2, fillvalue='')) if not char.isdigit())
