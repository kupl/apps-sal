import re


def solve(s):
    return max(map(len, re.findall('[uoiae]+', s)))
