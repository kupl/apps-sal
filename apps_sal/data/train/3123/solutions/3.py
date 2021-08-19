import re


def count_repeats(str):
    return len(str) - len(re.sub('(.)\\1+', '\\1', str))
