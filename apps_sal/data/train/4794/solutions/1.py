from collections import defaultdict


def comfortable_numbers(l, r):
    D, res = defaultdict(set), 0
    for i in range(l, r + 1):
        s = sum(map(int, str(i)))
        res += sum(i in D[j] for j in range(max(l, i - s), i))
        D[i] = set(range(i + 1, min(r, i + s) + 1))
    return res
