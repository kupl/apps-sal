from collections import Counter
def dominator(arr):
    [(e, c)] = Counter(arr).most_common(1) or [(-1, 0)]
    return [-1, e][2 * c > len(arr)]
