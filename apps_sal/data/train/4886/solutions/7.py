from collections import Counter

def find_dups_miss(arr):
    cnt = Counter(arr)
    dup = sorted(x for x in cnt if cnt[x] >= 2)
    miss = (set(xrange(min(cnt), max(cnt) + 1)) - set(cnt)).pop()
    return [miss, dup]
