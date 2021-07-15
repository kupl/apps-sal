def nba_extrap(ppg, mpg):
    return 0 if ppg == 0 and mpg == 0 else round(float(48 / mpg) * float(ppg), 1)
