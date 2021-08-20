import re


def replace_dots(str):
    replaced = re.sub('\\.', '-', str)
    return replaced
