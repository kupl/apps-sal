def nba_extrap(ppg, mpg):
    if ppg == 0:
        return 0
    else:
        full_time = 48
        average_points = ppg / mpg
        total_ppg = round(average_points * full_time, 1)
        return total_ppg
