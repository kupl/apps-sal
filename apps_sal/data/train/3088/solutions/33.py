def nba_extrap(ppg, mpg):
    if ppg != 0 and mpg != 0:
        return float('{0:.1f}'.format(ppg * 48 / mpg))
    else:
        return 0
