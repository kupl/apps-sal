def all_non_consecutive(a):
    return [{"i": i, "n": y} for i, (x, y) in enumerate(zip(a, a[1:]), 1) if x != y - 1]
