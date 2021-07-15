def nba_extrap(ppg, mpg):
    
    if mpg > 0:
        average = (ppg * 48)/ mpg
    else:
        average = 0 
    return round(average, 1)
