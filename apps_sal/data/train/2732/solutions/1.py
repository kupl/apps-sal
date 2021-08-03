from collections import Counter
from itertools import zip_longest


def blocks(s): return '-'.join(map(sortAndJoin, zip_longest(*blocker(s), fillvalue='')))
def sortAndJoin(lst): return ''.join(sorted(lst, key=blockKeyer))
def blockKeyer(c): return (c.isdigit(), c.isupper(), c)
def blocker(s): return (c * n for c, n in Counter(s).items())
