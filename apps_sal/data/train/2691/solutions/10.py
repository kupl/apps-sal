import re


def solve(s):
    reg = '(\\+?\\-?\\ *\\d+\\.?\\d*)'
    return max(map(float, re.findall(reg, s)))
