def growing_plant(u, d, h):
    days = growth = 0
    while True:
        days += 1
        growth += u
        if growth >= h:
            return days
        growth -= d
