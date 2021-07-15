def nba_extrap(ppg, mpg):
    return 0 if not mpg else round(ppg * 48 / mpg, 1)
