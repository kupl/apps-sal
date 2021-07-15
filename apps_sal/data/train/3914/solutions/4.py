from collections import Counter

def dominator(arr):
    n = Counter(arr).most_common(1)
    return n[0][0] if n and n[0][1] > len(arr)//2 else -1
