import sys

def nba_extrap(ppg, mpg):
    return round(ppg / (mpg + sys.float_info.epsilon) * 48, 1)
