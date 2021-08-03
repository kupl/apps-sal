import re


def solve(a, b):
    rx = '^' + '.*'.join(a.split('*')) + '$'
    return bool(re.search(rx, b))
