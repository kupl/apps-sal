from collections import Counter

def is_zero_balanced(arr):
    c = Counter(arr)
    return bool(arr) and all(c[k] == c[-k] for k in c)
