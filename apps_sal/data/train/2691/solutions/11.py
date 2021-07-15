import re

def solve(s):
    return max(int(x) for x in re.findall(r'[\d]+',s))
