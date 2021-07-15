def nba_extrap(ppg, mpg):
    return mpg and round(48 / mpg * ppg, 1)
