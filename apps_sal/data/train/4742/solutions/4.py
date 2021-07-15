from collections import Counter

def duplicates(a):
    return sum(e//2 for e in Counter(a).values())
