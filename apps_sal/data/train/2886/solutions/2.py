import re


def find(s):
    matches = [s for (s, _) in re.findall('((.)\\2*)', s)]
    return max((a + b for (a, b) in zip(matches, matches[1:])), key=len, default='')
