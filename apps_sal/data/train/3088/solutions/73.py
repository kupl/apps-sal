def nba_extrap(ppg, mpg):
    if not mpg or not ppg:
        return 0
    return round(48 / mpg * ppg, 1)
