def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    else:
        results = (ppg / mpg) * 48
        return round(results, 1)
