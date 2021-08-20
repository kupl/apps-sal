def fold_to(d):
    if d >= 0:
        return next((i for i in range(100) if 0.0001 * 2 ** i >= d))
