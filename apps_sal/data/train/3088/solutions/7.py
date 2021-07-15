def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    
    else:
        avgppm = ppg / mpg
        time = 48 - mpg
        guess = time * avgppm
        whole = (guess + ppg)
        return round(whole,1)
