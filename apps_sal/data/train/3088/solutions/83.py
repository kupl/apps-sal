def nba_extrap(ppg, mpg):
    if mpg == 48:
        return ppg
    elif mpg > 0:
        return round(ppg / mpg * 48, 1)
    else:
        return 0
