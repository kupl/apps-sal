import re


def lowercase_count(strng):
    r = re.compile('[a-z]')
    return len(r.findall(strng))
