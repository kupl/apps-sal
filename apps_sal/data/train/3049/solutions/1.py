import re


def textin(str):
    return re.sub('(?i)t[wo]?o', '2', str)
