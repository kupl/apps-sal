def evaporator(content, evap_per_day, threshold):
    n = 0
    x = 1-evap_per_day/100
    while x > threshold/100:
        x = x * (1-evap_per_day/100)
        n = n + 1
    return n+1
