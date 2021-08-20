import re


def remove(s):
    return ' '.join((m[0] for m in re.findall('((!*)\\w+\\2)', s)))
