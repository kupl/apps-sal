from collections import Counter

def highest_rank(arr):
    c = Counter(arr)
    return max(c, key=lambda x: (c[x], x))
