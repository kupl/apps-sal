def repeat_sum(l):
    f = [n for s in l for n in set(s)]
    return sum((n for n in set(f) if f.count(n) > 1))
