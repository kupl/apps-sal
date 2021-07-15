def nba_extrap(ppg, mpg):
    return round(ppg * 48 / (mpg or 1), 1)
