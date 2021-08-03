def nba_extrap(p, m):
    return round(float(p + (48 - m) / m * p), 1)
