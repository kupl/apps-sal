def nba_extrap(ppg, mpg):
    try:
        return round(ppg / mpg * 48, 1)
    except ZeroDivisionError:
        print("That can't be...")
