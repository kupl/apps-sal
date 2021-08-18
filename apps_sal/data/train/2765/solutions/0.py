import re


def compare(a, b):
    return a if specificity(a) > specificity(b) else b


def specificity(s):
    return [len(re.findall(r, s)) for r in (r'
