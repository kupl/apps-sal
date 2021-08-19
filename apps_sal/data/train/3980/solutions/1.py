import re


def reverse(strng):
    return re.sub('(\\w)\\1+', lambda m: m.group().swapcase(), strng)
