def nba_extrap(ppg, mpg):
    pt_min = ppg / mpg
    pt_min = pt_min * 48
    return round(pt_min, 1)
