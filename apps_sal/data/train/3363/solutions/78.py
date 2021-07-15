def evaporator(content, evap_per_day, threshold):
    days = 0
    thrshld = content*threshold/100
    while content >= thrshld:
        content -= content*evap_per_day/100
        days += 1
    return days
