def nba_extrap(ppg, mpg):
    return round(48*ppg/mpg if mpg else 0,1)
