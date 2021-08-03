import re


def solve(s):
    return max([int(d) for d in re.findall(r'\d{1,}', s)])
