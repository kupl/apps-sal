import re


def remove(s):
    return re.sub(r'!*?((!*)\w+\2)!*', r'\1', s)
