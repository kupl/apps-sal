def count(a, t, x):
    return sum(((e - t) % x == 0 if x != 0 else e - t == 0 for e in a))
