def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    else:
        ppm = ppg/mpg  
        full48 = ppm*48
        return round(full48, 1)
