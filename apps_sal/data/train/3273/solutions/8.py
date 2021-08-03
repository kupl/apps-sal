from collections import Counter


def solve(str1, str2):
    c1 = Counter(str1)
    for k, v in c1.items():
        if v >= 2 and k not in str2:
            return 1
    return 2
