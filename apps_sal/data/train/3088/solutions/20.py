nba_extrap = lambda ppg, mpg: 0 if mpg == 0 else round(ppg * (48 / mpg), 1)
