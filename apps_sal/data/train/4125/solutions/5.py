import re


def get_weight(name):
    return sum(map(ord, re.sub(r'[^a-zA-Z]', '', name.swapcase())))
