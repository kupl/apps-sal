import re


def lowercase_count(str):
    return len(re.findall('[a-z]', str))
