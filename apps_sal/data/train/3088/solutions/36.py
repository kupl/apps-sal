def nba_extrap(ppg, mpg):
    if ppg == mpg == 0:
        return 0
    else:
        return round((48*ppg)/mpg,1) 
