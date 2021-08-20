def nba_extrap(ppg, mpg):
    try:
        ppg = 48.0 * ppg / mpg
        return round(ppg, 1)
    except ZeroDivisionError:
        return 0
