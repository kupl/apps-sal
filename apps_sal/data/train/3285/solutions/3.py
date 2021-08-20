import re


def trump_detector(s):
    r = re.findall('a+|e+|i+|o+|u+', s, re.I)
    return round(sum((len(i) - 1 for i in r)) / len(r), 2)
