from collections import Counter


def solve(s):
    c = Counter(s)
    for key in c.keys():
        temp = Counter(key)
        check = c - temp
        if len(set(check.values())) < 2:
            return True
    return False
