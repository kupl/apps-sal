import re


def first_dup(s):
    return next(iter(re.findall('(.).*\\1', s)), None)
