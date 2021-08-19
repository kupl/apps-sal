import re


def has_subpattern(string):
    return bool(re.match('(.+)\\1+$', string))
