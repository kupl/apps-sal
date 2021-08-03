def nba_extrap(ppg, mpg): return round(ppg / (mpg * 1.0) * 48, 1) if mpg else 0
