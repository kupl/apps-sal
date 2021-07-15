def nba_extrap(ppg, mpg):
    if mpg!=0:
        points = (ppg/mpg)*48
    else: 
        points = 0
    return round(points,1)
