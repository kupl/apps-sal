import re


def solve(s):
    x = re.findall('[0-9]+', s)
    result = list(map(int, x))
    return(max(result))
