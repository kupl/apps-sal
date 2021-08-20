import re


def solve(s):
    kill = [int(x) for x in re.findall('[0-9]*', s) if x != '']
    return sorted(kill, reverse=True)[0]
