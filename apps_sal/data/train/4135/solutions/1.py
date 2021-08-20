from collections import Counter


def solve(s):
    c = Counter(s).values()
    (cVal, mi, ma) = (Counter(c), min(c), max(c))
    return len(cVal) <= 2 and (len(cVal) == 1 and (1 in cVal or 1 in cVal.values()) or mi == cVal[mi] == 1 or (mi == ma - 1 and cVal[ma] == 1))
