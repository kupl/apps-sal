def count(a, t, x):
    if x == 0:
        return a.count(t)
    return sum((t - e) % x == 0 for e in a)
