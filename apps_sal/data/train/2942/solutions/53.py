def fold_to(d):
    if d >= 0: return next(i for i in range(88) if 1e-4*2**i >= d)
