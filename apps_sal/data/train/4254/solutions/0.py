import re


def solve(eq):
    return ''.join(reversed(re.split('(\\W+)', eq)))
