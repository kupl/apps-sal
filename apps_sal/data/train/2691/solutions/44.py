import re

def solve(s):
    x = re.findall("\d+", s)
    x = list(map(int, x))
    return max(x)

