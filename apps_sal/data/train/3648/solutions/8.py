import re


def summy(s):
    return sum((int(e) for e in re.findall('\\d+', s)))
