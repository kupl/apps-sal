import re


def first_dup(s):
    return next(iter(re.findall(r'(.).*\1', s)), None)
