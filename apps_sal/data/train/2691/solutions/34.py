from re import findall


def solve(s):
    return max(map(int, findall('[\\d]{1,}', s)))
