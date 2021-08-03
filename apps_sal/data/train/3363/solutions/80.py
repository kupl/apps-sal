def evaporator(content, evap_per_day, threshold):
    maxthresh = content * threshold / 100
    amountevaporated = 0
    days = 0
    while content > maxthresh:
        percentage = evap_per_day / 100
        content = content - (content * percentage)
        days += 1
    return days
