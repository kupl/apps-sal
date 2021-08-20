def evaporator(content, evap_per_day, threshold):
    perc = 100
    days = 0
    while perc > threshold:
        perc = perc * (1 - evap_per_day / 100)
        days += 1
    return days
