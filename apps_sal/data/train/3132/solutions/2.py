from itertools import chain, zip_longest
def alternate_sort(l):
    return list(filter(lambda x: x is not None, chain(*zip_longest( sorted(filter(lambda x: x<0,l))[::-1],sorted(filter(lambda x: x>-1,l))))))
