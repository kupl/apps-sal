import re


def replace_dots(strg):
    return re.sub('\\.', '-', strg)
