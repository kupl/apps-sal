import re


def solve(s):
    return max(map(int, re.findall('\\d+', s)))
