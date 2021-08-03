def nba_extrap(ppg, mpg):
    if mpg != 0:
        ttl_scr = round(ppg / mpg * 48, 1)
        return ttl_scr
    else:
        return 0
