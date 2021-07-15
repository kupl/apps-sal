def repeats(a):
    return sum(filter(lambda x: a.count(x) < 2, a))
