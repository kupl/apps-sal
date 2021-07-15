def nba_extrap(ppg, mpg):
    extrap = (48 * ppg) / mpg
    return round(extrap, 1)


print(nba_extrap(5, 17))
