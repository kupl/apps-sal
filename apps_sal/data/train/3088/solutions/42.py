def nba_extrap(ppg, mpg):
    if ppg == 0:
        return 0
    else:
        num = ppg / mpg
        ans = num * 48
        ppg = round(ans, 1)
    return ppg
