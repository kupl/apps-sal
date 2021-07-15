def nba_extrap(ppg, mpg):
    tot_points = round(ppg/(mpg/48), 1)
    return tot_points 
