def nba_extrap(ppg, mpg):
    if ppg > 0:
        points_per_minute = ppg / mpg
        return round(points_per_minute * 48, 1)
    else:
        return 0
