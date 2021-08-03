def check(a, x):
    a.append(x)
    return bool(a.count(x) - 1)
