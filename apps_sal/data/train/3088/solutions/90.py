def nba_extrap(ppg, mpg):
    if mpg != 0:
        ppm = ppg/mpg    #point per minute they played
        ppg = round(ppm*48,1)
    else:
        ppg = 0
    return ppg



