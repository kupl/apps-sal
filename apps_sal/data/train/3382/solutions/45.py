import re


def lowercase_count(strng):
    pattern = re.compile('[a-z]{1}')
    matches = pattern.findall(strng)
    return len(matches)
