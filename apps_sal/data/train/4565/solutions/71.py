import re


def replace_dots(string):
    return re.sub('\\.', '-', string)
