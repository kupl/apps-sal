import re


def double_check(s):
    return bool(re.search('(.)\\1', s.lower()))
