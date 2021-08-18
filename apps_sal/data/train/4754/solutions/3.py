from itertools import groupby
from operator import itemgetter


def group_ints(lst, key=0):

    return list(map(list, map(itemgetter(1), groupby(lst, key.__gt__))))
