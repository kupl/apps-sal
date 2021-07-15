def evaporator(content, evap_per_day, threshold):
    day = 0
    contentRemaining = content
    
    while contentRemaining  > threshold * content / 100:
        contentRemaining -= evap_per_day / 100 * contentRemaining
        day += 1
    
    return day
