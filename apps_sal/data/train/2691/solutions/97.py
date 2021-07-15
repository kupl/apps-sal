import re

def solve(s):
    x = re.findall('[0-9]+', s)
    list = []
    for i in x:
        list.append(int(i))
    return max(list)
