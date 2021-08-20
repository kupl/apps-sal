from collections import Counter


def baby_count(x):
    c = Counter(x.lower())
    return min(c.get('b', 0) // 2, c.get('a', 0), c.get('y', 0)) or "Where's the baby?!"
