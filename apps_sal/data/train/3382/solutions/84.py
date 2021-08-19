import re


def lowercase_count(strng):
    lower = [c for c in strng if re.search('[a-z]', c)]
    return len(lower)
