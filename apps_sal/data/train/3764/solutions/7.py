import re


def arbitrate(s, _):
    p, m, b = s.partition('1')
    return p + m + '0' * len(b)
