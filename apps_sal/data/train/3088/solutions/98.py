def nba_extrap(ppg, mpg):
    if mpg != 0:
        ppg = ppg / mpg * 48
        return round(ppg, 1)
