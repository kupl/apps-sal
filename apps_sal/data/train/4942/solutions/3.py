from collections import Counter

def directions(goal):
    c = Counter(goal)
    for a, b in ['NS', 'EW']:
        m = min(c[a], c[b])
        c[a] -= m
        c[b] -= m
    return sorted(c.elements(), key='NSEW'.find)
