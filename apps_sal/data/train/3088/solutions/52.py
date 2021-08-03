def nba_extrap(ppg, mpg):

    if ppg == 0 or mpg == 0:
        return 0
    else:
        ppg_extrap = ppg / mpg * 48
    return round(ppg_extrap, 1)
