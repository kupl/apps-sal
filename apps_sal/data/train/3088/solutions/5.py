def nba_extrap(ppg, mpg):
    return round(48 * ppg/float(mpg), 1) if mpg != 0 else 0.
