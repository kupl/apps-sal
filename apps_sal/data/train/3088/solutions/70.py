def nba_extrap(ppg, mpg):
    if(mpg == 0):
        ppg = 0
    else:
        points_per_min = ppg / mpg
        ppg = round(points_per_min * 48, 1)
    return ppg
