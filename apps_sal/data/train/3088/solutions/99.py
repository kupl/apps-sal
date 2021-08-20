def nba_extrap(ppg, mpg):
    pts = 0
    if mpg > 0:
        pts = round(ppg / mpg * 48, 1)
    else:
        pass
    return pts
