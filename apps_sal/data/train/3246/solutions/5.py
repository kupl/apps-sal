from collections import Counter


def majority(arr):
    m = Counter(arr).most_common(2)
    return None if len(arr) == 0 or (len(m) == 2 and m[0][1] == m[1][1]) else m[0][0]
