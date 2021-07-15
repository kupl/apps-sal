import re

def solve(s):
    temp = re.findall(r'\d+', s)
    res = max(list(map(int, temp)))
    return res

