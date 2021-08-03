def nba_extrap(ppg, m):
    if m == 0 or ppg == 0:
        return 0
    full = 48 / m
    return round(ppg * full, 1)
