def evaporator(content, evap_per_day, threshold):
    hold = content*threshold / 100
    day = 0
    evap = evap_per_day / 100
    while (hold < content):
        content = content - content*evap
        day += 1
    return(day)
