import re


def double_check(strng):
    return bool(re.search('(.)\\1', strng, re.IGNORECASE))
