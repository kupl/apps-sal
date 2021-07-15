import re
def solve(s):
    g = re.findall(r'\d+',s)
    return max(map(int,g))
