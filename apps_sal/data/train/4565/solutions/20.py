import re


def replace_dots(s):
    print(s)
    return re.sub('\\.', '-', s)
