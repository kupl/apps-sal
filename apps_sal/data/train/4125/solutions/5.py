import re


def get_weight(name):
    return sum(map(ord, re.sub('[^a-zA-Z]', '', name.swapcase())))
