import re


def has_subpattern(s):
    return bool(re.search('^(.+)\\1+$', s))
