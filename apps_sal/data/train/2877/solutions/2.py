def count(a, t, x):
    return sum((x and (not (e - t) % x) or e - t == 0 for e in a))
