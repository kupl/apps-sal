from collections import Counter


def majority(arr):
    c = Counter(arr)
    t = c.most_common(2)
    if len(t) == 1 or (len(t) > 1 and t[1][1] < t[0][1]):
        return t[0][0]
    return None
