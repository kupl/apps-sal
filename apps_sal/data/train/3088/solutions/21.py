def nba_extrap(ppg, mpg):
    if ppg == 0 or mpg == 0:
        return 0
    overall_ppg = (ppg / mpg) * 48
    return float(("{:.1f}".format(overall_ppg)))
