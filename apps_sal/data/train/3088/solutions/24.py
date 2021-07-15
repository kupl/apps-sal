def nba_extrap(ppg, mpg):
    return round(48*float(ppg)/float(mpg),1) if mpg > 0 else 0
