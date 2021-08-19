def fold_to(d):
    if d >= 0:
        return next((i for i in range(88) if 0.0001 * 2 ** i >= d))
