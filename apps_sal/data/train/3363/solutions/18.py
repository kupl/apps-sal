def evaporator(content, evap_per_day, threshold):

    day = 0
    maxUse = content * (threshold / 100)
    evap = evap_per_day / 100
    while content > maxUse:
        content = content - content * evap
        day += 1

    return day
