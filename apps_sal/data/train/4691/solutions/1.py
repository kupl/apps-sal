import re


def solve(s):
    return [len(re.findall(i, s)) for i in ('[A-Z]', '[a-z]', '\\d', '[^a-zA-Z0-9]')]
