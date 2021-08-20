def nba_extrap(ppg, mpg):
    if mpg != 0:
        ppm = ppg / mpg
        ppg = round(ppm * 48, 1)
    else:
        ppg = 0
    return ppg
