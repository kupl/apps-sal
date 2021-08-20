from fractions import gcd
import re
from functools import reduce


def min_special_mult(arr):
    l = [e for e in arr if not re.match('(None)|([+-]?\\d+)', str(e))]
    if len(l) == 1:
        return 'There is 1 invalid entry: {}'.format(l[0])
    if len(l) > 1:
        return 'There are {} invalid entries: {}'.format(len(l), l)
    return reduce(lambda s, e: s * int(e) / gcd(s, int(e)) if e else s, arr, 1)
