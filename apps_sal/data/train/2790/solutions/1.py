import re


def dup(arry):
    return list(map(lambda s: re.sub('(\\w)\\1+', '\\1', s), arry))
