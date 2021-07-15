def count(a, t, x):
    return sum(not (t-v)%x if x else t==v for v in a)
