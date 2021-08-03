import re


def solve(s):
    b = re.findall('[0-9]+', s)
    return max([int(i) for i in b])
