def func(l):
    n = sum(l) // len(l)
    return [n] + [format(n, f) for f in "box"]
