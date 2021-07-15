def nba_extrap(ppg, mpg):
    try:
        return round(ppg/(mpg * 1.0)*48, 1) 
    except ZeroDivisionError:
        return 0

