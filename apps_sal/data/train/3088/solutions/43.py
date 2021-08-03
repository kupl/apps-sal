def nba_extrap(ppg, mpg):
    if ppg is 0:
        return 0
    else:
        return round((48 / mpg) * ppg, 1)
