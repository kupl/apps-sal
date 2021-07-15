def nba_extrap(ppg, mpg):
    return 0 if not mpg else round((ppg /float(mpg)) *48, 1)
