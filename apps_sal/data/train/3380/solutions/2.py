from itertools import groupby
from functools import reduce


def look_and_say_sequence(first_element, n):
    return reduce(lambda s, _: ''.join(('%d%s' % (len(list(g)), n) for (n, g) in groupby(s))), range(n - 1), first_element)
