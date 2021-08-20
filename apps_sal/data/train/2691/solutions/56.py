import re


def solve(s):
    return max((int(x) for x in re.split('\\D+', s) if x.isnumeric()))
