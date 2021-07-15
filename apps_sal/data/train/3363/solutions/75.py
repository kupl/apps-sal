def evaporator(content, evap_per_day, threshold):
    total = 1
    days=0
    while (total>threshold/100):
        total-= total*evap_per_day/100
        days+=1
    return days

