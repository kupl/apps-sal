import re


def solve(s):
    return max(map(int, re.findall('[0-9]+', s)))
