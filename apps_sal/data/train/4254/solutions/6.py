import re


def solve(eq):
    res = re.findall('([^0-9]+)|(\\d+)', eq)[::-1]
    return ''.join([a[::-1] + b for (a, b) in res])
