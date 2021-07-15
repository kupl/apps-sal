def nba_extrap(ppg, mpg):
    if mpg > 0:
        ppg = round ((ppg/mpg) * 48, 1)
    return ppg
