def indices(n, d):
    if d < 0:
        return []
    elif n == 1:
        return [[d]]
    elif n == 2:
        return [[i, d - i] for i in range(d + 1)]
    else:
        return [[i] + p for i in range(d + 1) for p in indices(n - 1, d - i)]
