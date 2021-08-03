import re


def solve(s):
    return max([int(i) for i in re.compile('[a-z]').split(s) if i != ''])
