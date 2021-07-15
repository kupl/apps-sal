def nba_extrap(ppg, mpg):
    newppg = (48/mpg) * ppg
    return round(newppg,1)

