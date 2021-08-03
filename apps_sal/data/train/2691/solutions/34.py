from re import findall


def solve(s):
    return max(map(int, findall(r"[\d]{1,}", s)))
