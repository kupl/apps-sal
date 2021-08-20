import re


def lowercase_count(strng):
    regex = '[a-z]'
    return len(re.findall(regex, strng))
