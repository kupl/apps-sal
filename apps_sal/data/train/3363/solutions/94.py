def evaporator(co, ev, th):
    x = co * (th / 100)
    day = 0
    while co > x:
        co = co - co * (ev / 100)
        day += 1
    return day
