def nba_extrap(ppg, mpg):
    total_min = 48
    if mpg == 0:
        return 0
    else:
        ppm = ppg / mpg  # points per minute
        res = ppm * total_min
        return round(res, 1)
