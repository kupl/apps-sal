def nba_extrap(ppg, mpg):
    return round(ppg / (mpg / 48 * 100) * 100, 1)
