import re


def solve(s):
    return max([int(x) for x in re.compile('\\D').split(s) if x != ''])
