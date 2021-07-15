def nba_extrap(ppg, mpg):
    return 0 if ppg == False else round(48 * ppg / mpg, 1)
