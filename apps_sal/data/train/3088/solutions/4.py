def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    else:
        return round(ppg*48.0/mpg, 1) 



