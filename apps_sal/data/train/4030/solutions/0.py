from itertools import groupby
from operator import itemgetter
from os.path import commonprefix
first = itemgetter(0)


def radix_tree(*words):
    words = [w for w in words if w]
    result = {}
    for (key, grp) in groupby(sorted(words), key=first):
        lst = list(grp)
        prefix = commonprefix(lst)
        result[prefix] = radix_tree(*(w[len(prefix):] for w in lst))
    return result
