import re


def replace_dots(str):
    a = re.sub('\\.', '-', str)
    return a
