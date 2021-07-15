def evaporator(content, evap_per_day, threshold):
    n = 0
    perc = 100
    while perc > threshold:
        perc *= 1 - evap_per_day / 100
        n += 1
    return n
