import re


def replace_dots(s):
    s = re.sub('\\.', '-', s)
    return s
