import re

def solve(s):
    temp = re.findall(r'\d+', s)
    erg = list(map(int, temp))
    return int(max(erg))
