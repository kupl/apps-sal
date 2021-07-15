from collections import Counter

def repeats(arr):
    return sum(k for k, v in Counter(arr).items() if v == 1)
