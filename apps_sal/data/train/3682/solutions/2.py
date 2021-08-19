import re


def string_constructing(a, s):
    n = len(re.findall('?'.join(list(a)) + '?', s)) - 1          # "-1" because one empty string is always found at the end
    return n + len(a) * n - len(s)
