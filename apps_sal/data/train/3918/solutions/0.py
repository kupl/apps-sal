def baby_count(x):
    x = x.lower()
    return min(x.count('a'), x.count('b') // 2, x.count('y')) or "Where's the baby?!"
