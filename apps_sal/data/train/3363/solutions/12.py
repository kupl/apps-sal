def evaporator(content, evap_per_day, threshold):
    day = 0
    p = content/100*threshold
    while content >= p:
        day+=1
        perc = content / 100 * evap_per_day
        content -= perc
    return day

