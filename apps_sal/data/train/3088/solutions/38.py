def nba_extrap(ppg, mpg):
    if ppg == 0 or mpg == 0:
        return 0
    pointsPerMinute = ppg / mpg
    ppg = pointsPerMinute * 48
    total = round(ppg, 1)
    return total
