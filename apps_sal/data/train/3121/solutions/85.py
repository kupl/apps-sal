from collections import Counter


def solve(arr):
    c = Counter(arr)
    for k, v in c.items():
        if (k * -1) not in c.keys():
            return k
