from collections import Counter

def bucketize(*arr):
    c = Counter(arr)
    return [sorted(k for k,v in c.items() if v==i) if i in c.values() else None for i in range(len(arr)+1)]
