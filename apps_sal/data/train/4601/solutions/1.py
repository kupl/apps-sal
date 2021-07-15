def mormons(start, fac, target):
    return 0 if start >= target else 1 + mormons(start * (fac + 1), fac, target)
