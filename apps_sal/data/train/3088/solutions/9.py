def nba_extrap(ppg, mpg):
    try:
        return round(float(ppg) / mpg * 48, 1)
    except:
        return 0
