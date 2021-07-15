from collections import Counter
from itertools import count, islice

def performant_smallest(arr, n):
    cnts = Counter(arr)
    total = 0
    for i, c in sorted(cnts.items()):
        total += c
        if total >= n:
            break
    available = count(c + n - total, -1)
    it = (x for x in arr if x < i or (x == i and next(available) > 0))
    return list(islice(it, n))
