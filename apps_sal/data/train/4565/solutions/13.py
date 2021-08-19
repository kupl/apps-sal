import re


def replace_dots(s):
    x = re.sub('[.]', '-', s)
    return x
