def nba_extrap(ppg, mpg):
    alt_ppg = ppg / mpg * 48
    return round(alt_ppg,1)
