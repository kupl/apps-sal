def evaporator(content, evap_per_day, threshold):
    n = 0
    perc = 100
    perc_per_day = 1 - evap_per_day / 100
    while perc > threshold:
        perc *= perc_per_day
        n += 1
    return n
