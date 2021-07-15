def nba_extrap(ppg, mpg):
    if ppg == 0:
        ppg = 0
    else:
        ppg = round((ppg/mpg) * 48, 1)
    return ppg
