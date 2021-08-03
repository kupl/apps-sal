def nba_extrap(ppg, mpg):
    return round(ppg * 48 / mpg, 1) if mpg else 0
