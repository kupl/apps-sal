def nba_extrap(ppg, mpg):
    return round(ppg * 48 / mpg if mpg else 0, 1)
