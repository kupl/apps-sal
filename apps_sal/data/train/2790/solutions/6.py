import re


def dup(xs):
    return [re.sub(r'(.)\1+', r'\1', x) for x in xs]
