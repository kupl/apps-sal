import re


def solve(s):
    return max(len(x.group(0)) for x in re.finditer(r'[aeiou]+', s))
