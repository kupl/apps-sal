def evaporator(x, y, z):
    content = x
    evap_per_day = y
    treshold = z
    perc_th = treshold / 100
    perc_evap = evap_per_day / 100
    min_content = content * perc_th
    total_days = 0
    while content >= min_content:
        content -= content * perc_evap
        total_days += 1
    return total_days
