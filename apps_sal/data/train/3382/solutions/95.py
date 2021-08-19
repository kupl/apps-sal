import re


def lowercase_count(strng):
    matches = re.findall('[a-z]', strng)
    return len(matches)
