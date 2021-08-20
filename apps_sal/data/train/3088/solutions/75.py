def nba_extrap(ppg, mpg):
    if ppg and mpg:
        return round(ppg / mpg * 48, 1)
    else:
        return 0
