import re


def replace_dots(str):
    new = re.sub('\\.', '-', str)
    return new
