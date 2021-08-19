def find_dups_miss(arr):
    from collections import Counter
    dup = sorted([i for (i, cnt) in Counter(arr).items() if cnt > 1])
    miss = list(set(range(min(arr), max(arr) + 1)) - set(arr))
    return [miss[0], dup]
