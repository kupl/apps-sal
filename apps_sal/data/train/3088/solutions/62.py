def nba_extrap(ppg, mpg):
    full_match = 48
    ppmpm = ppg/mpg
    return round(ppmpm * full_match, 1)

