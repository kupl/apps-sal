import re


def double_check(strng):
    pattern = re.compile('(.)\\1', re.IGNORECASE)
    return bool(re.search(pattern, strng))
