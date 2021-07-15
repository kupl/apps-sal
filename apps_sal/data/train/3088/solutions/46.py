import math
def nba_extrap(ppg, mpg):
    try:
        ppg = (ppg*48)/mpg
        ppg = round(ppg,1)
    except ZeroDivisionError:
        ppg = 0
    return ppg


