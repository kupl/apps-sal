from collections import defaultdict


def fix_progression(arr):
    res = 0
    for i in range(len(arr)):
        D = defaultdict(int)
        for j in range(i):
            q, r = divmod(arr[i] - arr[j], i - j)
            if not r:
                D[q] += 1
                res = max(res, D[q])
    return len(arr) - res - 1
