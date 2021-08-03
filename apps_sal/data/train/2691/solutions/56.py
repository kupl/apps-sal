import re


def solve(s):
    return max(int(x) for x in re.split(r'\D+', s) if x.isnumeric())
