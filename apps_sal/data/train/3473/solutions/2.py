import re


def doubles(s):
    re_double = re.compile('(.)\\1')
    while re_double.search(s):
        s = re_double.sub('', s)
    return s
