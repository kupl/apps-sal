from collections import Counter

def baby_count(s):
    c = Counter(s.lower())
    return min(c['a'],c['b']//2,c['y']) or "Where's the baby?!"
