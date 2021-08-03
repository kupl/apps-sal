from collections import Counter


def majority(arr):
    mc = Counter(arr).most_common(2)
    if arr and (len(mc) == 1 or mc[0][1] != mc[1][1]):
        return mc[0][0]
