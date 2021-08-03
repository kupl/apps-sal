import re


def lowercase_count(st):
    return len(re.sub(r'[^a-z]*', '', st))
