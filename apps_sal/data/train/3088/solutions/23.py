def nba_extrap(ppg, mpg):
    return float('%0.1f' % (48 * ppg / mpg)) if ppg > 0 else 0
