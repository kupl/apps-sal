nba_extrap = lambda ppg, mpg: round(ppg/(mpg*1.0)*48, 1) if mpg else 0
