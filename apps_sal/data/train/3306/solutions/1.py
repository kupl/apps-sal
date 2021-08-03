import re


def solve(a, b):
    return bool(re.fullmatch(a.replace('*', '.*'), b))
