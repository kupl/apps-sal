import re


def solve(s):
    temp = re.findall('\\d+', s)
    erg = list(map(int, temp))
    return int(max(erg))
