def nba_extrap(ppg, mpg):
    try:        
        ppg = ppg * (48/mpg)
        ppg = round(ppg, 1)
        return ppg 
    except ZeroDivisionError:
        return 0
