import re


def dup(xs):
    return [re.sub('(.)\\1+', '\\1', x) for x in xs]
