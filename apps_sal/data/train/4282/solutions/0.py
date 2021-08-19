import re


def hungry_seven(arr):
    (ss, s) = ('', ''.join(map(str, arr)))
    while ss != s:
        (ss, s) = (s, re.sub('(7+)(89)', '\\2\\1', s))
    return list(map(int, s))
