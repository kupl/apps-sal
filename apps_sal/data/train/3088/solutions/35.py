def nba_extrap(ppg, mpg):
    points_per_min = ppg / mpg
    points_per_game = round(points_per_min * 48, 1)
    return points_per_game
