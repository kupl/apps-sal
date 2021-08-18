import re


def solve(a, b):
    return bool(re.match(f"^{a.replace('*', '.*')}$", b))
