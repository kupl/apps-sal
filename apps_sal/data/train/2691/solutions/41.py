import re


def solve(string):
    return max(map(int, re.findall('[\\d]+', string)))
