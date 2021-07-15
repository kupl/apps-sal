def nba_extrap(ppg, mpg):
    uebrig = 48 / mpg
    if (mpg != 48):
        loesung = (ppg * uebrig)
        return round(loesung, 1)
    else:
        print(0)
