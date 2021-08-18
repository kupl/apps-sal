import re


def string_constructing(a, s):
    n = len(re.findall('?'.join(list(a)) + '?', s)) - 1
    return n + len(a) * n - len(s)
