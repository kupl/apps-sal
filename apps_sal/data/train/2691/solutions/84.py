import re


def solve(var):
    return max((int(x) for x in re.findall('\\d+', var)))
