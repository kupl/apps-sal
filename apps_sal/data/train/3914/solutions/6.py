from collections import Counter

def dominator(arr):
    xs = Counter(arr).most_common(1)
    if xs and (xs[0][1] > len(arr) // 2):
        return xs[0][0]
    return -1
