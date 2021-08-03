import re


def has_subpattern(s):
    return bool(re.search(r'^(.+)\1+$', s))
