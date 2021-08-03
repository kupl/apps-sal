from decimal import Decimal


def nba_extrap(ppg, mpg):
    return float(round(Decimal(ppg * 48 / mpg), 1))
