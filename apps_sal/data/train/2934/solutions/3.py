import re


def solve(s):
    return max((sum((ord(x) - 96 for x in c)) for c in re.split('[aeiou]', s)))
