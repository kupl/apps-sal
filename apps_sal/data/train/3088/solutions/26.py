def nba_extrap(ppg, mpg):
    if ppg == 0:
        return 0
    ppg = (ppg * 48)/ mpg
    return round(ppg,1)
