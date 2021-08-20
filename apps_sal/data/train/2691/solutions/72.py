import re


def solve(s):
    return max((int(n or '0') for n in re.split('[a-z]+', s)))
