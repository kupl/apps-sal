import re


def solve(s):
    return max(sum(ord(c) - 96 for c in subs) for subs in re.split('[aeiou]+', s))
