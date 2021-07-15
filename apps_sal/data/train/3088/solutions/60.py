def nba_extrap(ppg, mpg):
    if mpg == 0 or ppg == 0:
        return 0
    else:
        return round(round((48/mpg)*ppg,1),10)
