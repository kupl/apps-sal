def nba_extrap(ppg, mpg):
    if mpg != 0:
        yep = 48 / mpg
        return round(yep * ppg, 1)
    else:
        return 0
