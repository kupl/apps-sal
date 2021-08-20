import re


def reverse(s):
    return re.sub('(.)\\1+', lambda m: m.group().swapcase(), s)
