def nba_extrap(ppg, mpg):
    # ppg / mpg = ppgNew / 48
    # ppg(48) / mpg
    if mpg == 0:
        return 0
    return round(ppg * 48 / mpg, 1)
