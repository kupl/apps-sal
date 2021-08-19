import re


def solve(s):
    l = [int(i) for i in re.findall('(\\d+)', s)]
    return max(l)
