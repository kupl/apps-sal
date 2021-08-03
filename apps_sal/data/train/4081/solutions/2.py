def first_tooth(xs):
    diff = [(x - xs[i - 1] if i > 0 else 0) + (x - xs[i + 1] if i + 1 < len(xs) else 0) for i, x in enumerate(xs)]
    x = max(diff)
    if diff.count(x) > 1:
        return -1
    return diff.index(x)
