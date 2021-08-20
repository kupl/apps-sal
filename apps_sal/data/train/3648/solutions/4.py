import re


def summy(s):
    return sum(map(int, re.split('[^\\d]+', s)))
