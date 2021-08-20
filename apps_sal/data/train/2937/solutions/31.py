def between(a, b):
    c = range(a, b + 1, 1)
    return [x for x in c if x >= a]
