def nba_extrap(ppg, mpg):
    if mpg == 0 or ppg == 0:
        return 0
    average = 48 / mpg
    ppg = round(average * ppg * 10) / 10
    return ppg
