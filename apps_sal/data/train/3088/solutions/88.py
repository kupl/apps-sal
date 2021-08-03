def nba_extrap(ppg, mpg):
    try:
        ppg = ppg / mpg * 48
        return round(ppg, 1)
    except ZeroDivisionError:
        return 0
