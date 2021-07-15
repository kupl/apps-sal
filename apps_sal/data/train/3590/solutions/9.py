from collections import Counter


def solve(arr_1, arr_2):
    cnt = Counter(arr_1)
    return [cnt[a] for a in arr_2]

