def nba_extrap(ppg, mpg):
    if ppg != 0 or mpg != 0:
        return round(ppg * 48 / mpg, 1)
    else:
        return 0
