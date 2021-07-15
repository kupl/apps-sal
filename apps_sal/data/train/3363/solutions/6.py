def evaporator(content, evap_per_day, threshold):
    print(content, evap_per_day, threshold)
    i = 0
    c = 1
    while c >= threshold/100:
        c *= 1 - evap_per_day/100
        i += 1
    return i
