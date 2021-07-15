def nba_extrap(ppg, mpg):
    ppg1 = mpg  / 48 * 100
    ppg1 = ppg / ppg1 * 100 
    ppg1 = round(ppg1,1)
    return ppg1
