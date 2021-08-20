import re


def lowercase_count(strng):
    regex = re.compile('[a-z]')
    match = regex.findall(strng)
    if match:
        return len(match)
    return 0
