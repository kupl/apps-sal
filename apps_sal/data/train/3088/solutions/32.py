def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    else:
        avg = 48 / mpg
        ppg = ppg * avg
        return round(ppg, 1)
