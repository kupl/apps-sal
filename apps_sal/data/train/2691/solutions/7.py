import re


def solve(s):
    g = re.findall('\\d+', s)
    return max(map(int, g))
