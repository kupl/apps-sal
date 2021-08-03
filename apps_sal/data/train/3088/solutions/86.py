def nba_extrap(ppg, mpg):
    x = ppg * 48.0 / mpg
    return round(x, 1)
