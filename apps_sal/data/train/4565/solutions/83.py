import re


def replace_dots(str):
    print(str)
    return re.sub('\\.', '-', str)
