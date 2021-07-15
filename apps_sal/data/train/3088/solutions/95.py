def nba_extrap(ppg, mpg):
    full_ppg = 0
    if ppg == 0:
        return 0
    return round((ppg*48) / mpg, 1)
