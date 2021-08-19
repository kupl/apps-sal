import re
from itertools import zip_longest


def next_version(version):
    (s, n) = re.subn('\\.', '', version)
    return ''.join([b + a for (a, b) in zip_longest('{:0{}}'.format(int(s) + 1, len(s))[::-1], '.' * n, fillvalue='')][::-1])
