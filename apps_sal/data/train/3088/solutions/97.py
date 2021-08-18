def nba_extrap(ppg, mpg):
    try:
        relative_minutes = (48 / mpg)
        relative_points = round(ppg * relative_minutes, 1)
    except:
        relative_points = 0
    return relative_points
