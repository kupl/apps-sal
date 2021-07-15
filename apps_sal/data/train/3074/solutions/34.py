def growing_plant(u, d, h):
    days = growth = 0
    
    while True:
        # day
        days += 1
        growth += u

        if growth >= h:
            return days
        
        # night
        growth -= d
