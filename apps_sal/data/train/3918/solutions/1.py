from collections import Counter

def baby_count(x):
    c = Counter(x.lower())
    return min(c['b'] // 2, c['a'], c['y']) or "Where's the baby?!"
