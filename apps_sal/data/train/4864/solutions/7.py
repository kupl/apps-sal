import re


def remove(s):
    return re.sub('!*?((!*)\\w+\\2)!*', '\\1', s)
