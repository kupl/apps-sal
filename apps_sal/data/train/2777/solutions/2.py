import re


def solve(st):
    matches = re.match('([a-z]*)(\\d*)\\((.*)\\)', st)
    if not matches:
        return st
    return matches.group(1) + (int(matches.group(2)) if matches.group(2) else 1) * solve(matches.group(3))
