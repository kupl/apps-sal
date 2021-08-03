def closest_pair_tonum(lim):
    return next((m, n) for m in range(lim - 1, 0, -1) for n in range(m - 1, 0, -1) if not ((m + n)**0.5 % 1 or (m - n)**0.5 % 1))
