import re
def solve(s):
    return max(map(int, re.findall(r'[0-9]+', s)))
